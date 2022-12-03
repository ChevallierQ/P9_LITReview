from re import template
from sqlite3 import connect
from tkinter.tix import Form
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import forms, models
from django.conf import settings
from django.views.generic import View


class LoginPage(View):
    """
        Class LoginPage is the view using to manage the user login page.
    """
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        """
            Def get is the function using to get the login form.
        """
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        """
            Def post is the function using to connect the user.
        """
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
    """
        Def logout_page is the function using to disconnect the user.
    """
    logout(request)
    return redirect('login')


def signup_page(request):
    """
        Def signup_page is the view using to manage the user signup page.
    """
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flux')
    return render(request, 'authentication/signup.html', context={'form': form})


def profil_page(request):
    """
        Def profil_page is the function using to access at the user profil manager.
    """
    return render(request, 'profil/profil.html')


def profil_modify_page(request, id):
    """
        Def profil_modify_page is the view using to manage the user profil page.
    """
    profil = models.User.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ProfilForm(request.POST, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = forms.ProfilForm(instance=profil)

    return render(request, 'profil/profil_modify.html', {'form': form})


def profil_delete(request, id):
    """
        Def profil_delete is the function using to delete the user profil.
    """
    profil = models.User.objects.get(id=id)
    if request.method == 'POST':
        profil.delete()
        return redirect('login')

    