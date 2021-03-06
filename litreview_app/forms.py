from dataclasses import field
from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image',]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body',]


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['followed_user',]
