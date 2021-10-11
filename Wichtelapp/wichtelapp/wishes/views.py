from django.shortcuts import render
from .forms import WishForm, TakeWish, WishSentForm
from django.db import models
from .models import Wish
from users.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from random import shuffle
from datetime import datetime
from django.utils import timezone

# Create your views here.

@login_required
def wish_detail_view(request):
    obj = Wish.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'wishes/wish_detail.html', context)

@login_required
def wish_approve_view(request):
    if request.method == 'POST':
        wishsent = Wish.objects.filter(wisher=request.user).filter(state='Sent')
        if wishsent:
            for wish in wishsent:
                wish.state = 'Received'
                wish.received = timezone.now()
                wish.save()
                return HttpResponseRedirect('/approve')
        return HttpResponseRedirect('/approve')
    return render(request, 'wishes/wish_approve.html')



@login_required
def wish_todo_view(request):
    takenwishes = Wish.objects.filter(secret_santa=request.user)
    data = {}
    for wish in takenwishes:
        data[wish] = wish.wisher.profile

    if request.method == 'POST':
        r = request.POST.get('wishid', default=None)
        requestedwish = Wish.objects.get(id=r)
        form = WishSentForm(request.POST, instance=requestedwish)
        if form.is_valid():
            question = form.save(False)
            question.sent = timezone.now()
            question.state = 'Sent'
            form.save()
            return HttpResponseRedirect('/todo')

    context = {
    'wishes': takenwishes,
    'data': data,
    'form': WishSentForm
    }
    return render(request, 'wishes/wish_todo.html', context)




    



@login_required
def wish_create_view(request):
    submitted = False
    if Wish.objects.filter(wisher=request.user).count() >= 3:
        return render(request, 'wishes/wish_create.html', {'notAllowed': True})
    if request.method == 'POST':

        form = WishForm(request.POST)
        if form.is_valid():
            question = form.save(False)
            question.wisher = request.user
            if Wish.objects.filter(wisher=request.user).filter(is_visible=False).count() >= 1:
                question.is_visible = False
            form.save()
            return HttpResponseRedirect('/create?submitted=True')
    else:
        form = WishForm
        if 'submitted' in request.GET:
            submitted = True
    form = WishForm
    return render(request, 'wishes/wish_create.html', {'form':form, 'submitted':submitted, 'notAllowed': False})

@login_required
def wish_list_view(request):
    submitted = False
    if request.method == 'POST':
        r = request.POST.get('wishid', default=None)
        requestedwish = Wish.objects.get(id=r)
        form = TakeWish(request.POST, instance=requestedwish)
        if form.is_valid():
            question = form.save(False)
            question.secret_santa = request.user
            question.taken = timezone.now()
            question.is_visible = False
            question.state = 'Taken'
            form.save()
            openwishes = Wish.objects.filter(wisher=requestedwish.wisher).filter(is_visible=True)
            if openwishes: 
                for openwish in openwishes:
                    openwish.is_visible = False
                    openwish.save()
            print(request.POST)
        return HttpResponseRedirect('/wishlist?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
        is_allowed = True
        openwishes = Wish.objects.filter(secret_santa=request.user).exclude(state='Received').exclude(state='Sent').count()
        if openwishes:
            is_allowed = False
        allopenwishes = list(Wish.objects.all().exclude(wisher=request.user).exclude(is_visible=False))
        shuffle(allopenwishes)
        context= {
        'wishes': allopenwishes,
        'is_allowed': is_allowed,
        'submitted': submitted
        }
        return render(request, 'wishes/wish_list.html', context)