from pyexpat import model
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template import context
from . import models
from . import forms



@login_required
def subscription(request):
    return render(request, 'subscription/subscription.html')
  

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


@login_required
def review_without_ticket(request):
    ticket_form = forms.TicketForm()
    review_without_ticket_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = ticket()
        review_without_ticket_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_without_ticket_form.is_valid()]):
            review_without_ticket = review_without_ticket_form.save(commit=False)
            review_without_ticket.user = request.user
            review_without_ticket.save()
            return redirect('flux')
    context = {
        'ticket_form': ticket_form,
        'review_without_ticket_form': review_without_ticket_form
    }
    return render(request, 'review/review_without_ticket.html', context=context)


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'flux/flux.html', context={'tickets': tickets})