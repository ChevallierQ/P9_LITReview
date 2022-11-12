from re import template
from sqlite3 import connect
from tkinter.tix import Form
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.conf import settings
from django.views.generic import View


class LoginPage(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('flux')
            else :
                message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})


def logout_page(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flux')
    return render(request, 'authentication/signup.html', context={'form': form})


def profil_page(request):
    return render(request, 'profil/profil.html')


def profil_modify_page(request):
    return render(request, 'profil/profil_modify.html')
    