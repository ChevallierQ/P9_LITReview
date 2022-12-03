from asyncio import MultiLoopChildWatcher
from audioop import reverse
from hashlib import new
from pickle import TRUE
from pyexpat import model
from random import random
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template import context
from . import models
from . import forms
from authentification import models as modelsA


@login_required
def subscription(request):
    """
        Def subscription is the view using to manage a relation between two user.
    """
    form = forms.FollowUsersForm()
    users = modelsA.User.objects.all()
    follow_model = models.UserFollows.objects.all()
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST)
        if form.is_valid():
            follow_list = list(models.UserFollows.objects.all())
            follow_list.sort(key=lambda x: x.user_id)
            follow = form.save(commit=False)
            list_couple = list()
            for element in follow_list:
                couple = (element.user, element.followed_user)
                list_couple.append(couple)
            new_couple = (request.user, follow.followed_user) 
            if new_couple not in list_couple:
                if request.user != follow.followed_user:
                    follow.user = request.user
                    follow.save()
                else:
                    pass
            else:
                pass

    context = {
        'form': form,
        'users': users,
        'follow_model': follow_model,
    }  
    return render(request, 'subscription/subscription.html', context=context)


def subscription_unfollow(request, id):
    """
        Def subscription_unfollow is the function using to unfollow a user.
    """
    unfollow = models.UserFollows.objects.get(id=id)
    if request.method == 'POST':
        unfollow.delete()
        return redirect('subscription')


@login_required
def posts(request):
    """
        Def posts is the view using to manage the posts page.
    """
    self_posts = list(models.Ticket.objects.all())
    self_review = list(models.Review.objects.all())
    for element in self_review:
        self_posts.append(element)
    return render(request, 'posts/posts.html', context={'self_posts': self_posts})


@login_required
def ticket(request):
    """
        Def ticket is the view using to manage the ticket page.
    """
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
    """
        Def ticket_detail is the view using to manage the ticket_modify page.
    """
    ticket = models.Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = forms.TicketForm(instance=ticket)
    return render(request, 'posts/ticket_modify.html', {'form': form})


def review_detail(request, id):
    """
        Def review_detail is the view using to manage the review_modify page.
    """
    review = models.Review.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = forms.ReviewForm(instance=review)
    return render(request, 'posts/review_modify.html', {'form': form})


def ticket_delete(request, id):
    """
        Def ticket_delete is the function using to delete a ticket.
    """
    ticket = models.Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('posts')


def review_delete(request, id):
    """
        Def review_delete is the function using to delete a review.
    """
    review = models.Review.objects.get(id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('posts')


@login_required
def review_without_ticket(request):
    """
        Def review_without_ticket is the view using to manage the review_without_ticket page.
    """
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
def review_with_ticket(request, id):
    """
        Def review_with_ticket is the view using to manage the review_with_ticket page.
    """
    ticket = models.Ticket.objects.get(id=id)
    review_with_ticket_form = forms.ReviewForm()
    if request.method == "POST":
        ticket = forms.TicketForm(request.POST, instance=ticket)
        review_with_ticket_form = forms.ReviewForm(request.POST)
        if review_with_ticket_form.is_valid():
            review_with_ticket = review_with_ticket_form.save(commit=False)
            review_with_ticket.user = request.user
            review_with_ticket.save()
            return redirect('flux')
    context = {
        'ticket': ticket,
        'review_with_ticket_form': review_with_ticket_form,
    }
    return render(request, 'review/review_with_ticket.html', context=context)


@login_required
def home(request):
    """
        Def home is the view using to manage the flux page.
    """
    reviews = list(models.Review.objects.all())
    tickets = list(models.Ticket.objects.all())
    follow = models.UserFollows.objects.all()
    reviews_tickets = reviews + tickets
    reviews_tickets.sort(key=lambda x: x.time_created, reverse=True)
    reviews_headline = []
    for review_unit in reviews :
        reviews_headline.append(review_unit.headline)
    context = {
            'reviews_tickets': reviews_tickets,
            'reviews_headline': reviews_headline,
            'follows': follow,
        }
    return render(request, 'flux/flux.html', context=context)
