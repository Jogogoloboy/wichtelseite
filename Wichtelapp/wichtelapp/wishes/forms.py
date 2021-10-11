from django import forms
from django.forms import ModelForm
from .models import Wish



class WishForm(ModelForm):
    class Meta:
        model = Wish
        fields = [
        'title',
        'description',
        'category',
        'difficulty'
        ]

class TakeWish(ModelForm):
    class Meta:
        model = Wish
        fields = ['taken', 'secret_santa', 'is_visible']

class WishSentForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields= ['trackingnr']

