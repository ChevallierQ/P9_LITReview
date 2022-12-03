from dataclasses import fields
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class LoginForm(forms.Form):
    """
        Class LoginForm is the form using for the user connexion.
    """
    username = forms.CharField(max_length=63, label='Username ')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Password ')


class SignupForm(UserCreationForm):
    """
        Class SignupForm is the form using to create a user account by using the native form UserCreationForm.
    """
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)


class ProfilForm(forms.ModelForm):
    """
        Class ProfilForm is the form using to modify a user profil.
    """
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email',]