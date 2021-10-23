from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'favoritecolors', 'favoritematerials', 'favoritesmells', 'favoritefood', 'favoritestyles', 'idontlike', 'allergies', 'accessories', 'sizes', 'nerdlove', 'characters', 'other', 'pinterest', 'image1', 'image2', 'image3']