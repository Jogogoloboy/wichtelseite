from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print (request.user)
    return render(request, "pages/home.html", {})

def impressum_view(request, *args, **kwargs):
    return render(request, "pages/impressum.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "pages/about.html", {})