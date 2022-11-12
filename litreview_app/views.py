from asyncio import MultiLoopChildWatcher
from pyexpat import model
from random import random
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template import context
from . import models
from . import forms
from authentification import models as modelsA


@login_required
def subscription(request):
    form = forms.FollowUsersForm()
    users = modelsA.User.objects.all()
    follow_model = models.UserFollows.objects.all()
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST)
        if form.is_valid():
            follow = form.save(commit=False)
            follow.user = request.user
            follow.save()

    context = {
        'form': form,
        'users': users,
        'follow_model': follow_model,
    }  
    return render(request, 'subscription/subscription.html', context=context)


@login_required
def posts(request):
    self_posts = list(models.Ticket.objects.all())
    self_review = list(models.Review.objects.all())
    for element in self_review:
        self_posts.append(element)
    return render(request, 'posts/posts.html', context={'self_posts': self_posts})


@login_required
def ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    context = {
        'ticket_form': ticket_form,
    }   
    return render(request, 'ticket/ticket.html', context=context)



def ticket_detail(request, id):
    ticket = models.Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('posts', ticket.id)
    else:
        form = forms.TicketForm(instance=ticket)
    return render(request, 'posts/ticket_modify.html', {'form': form})


def review_detail(request, id):
    review = models.Review.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('posts', review.id)
    else:
        form = forms.ReviewForm(instance=review)
    return render(request, 'posts/review_modify.html', {'form': form})


def ticket_delete(request, id):
    ticket = models.Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('posts')


def review_delete(request, id):
    review = models.Review.objects.get(id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('posts')





@login_required
def review_without_ticket(request):
    ticket_form = forms.TicketForm()
    review_without_ticket_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_without_ticket_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_without_ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review_without_ticket = review_without_ticket_form.save(commit=False)
            review_without_ticket.user = request.user
            review_without_ticket.ticket = ticket
            review_without_ticket.save()
            return redirect('flux')
    context = {
        'ticket_form': ticket_form,
        'review_without_ticket_form': review_without_ticket_form
    }
    return render(request, 'review/review_without_ticket.html', context=context)


@login_required
def home(request):
    reviews = list(models.Review.objects.all())
    tickets = list(models.Ticket.objects.all())
    follow = models.UserFollows.objects.all()
    reviews_headline = []
    for review_unit in reviews :
        reviews_headline.append(review_unit.headline)
    context = {
            'tickets': tickets,
            'reviews': reviews,
            'reviews_headline': reviews_headline,
            'follows': follow,
        }
    return render(request, 'flux/flux.html', context=context)
