from dataclasses import field
from django import forms
from . import models


class TicketForm(forms.ModelForm):
    """
        Class TicketForm is the form using for the ticket creation.
    """
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image',]

class ReviewForm(forms.ModelForm):
    """
        Class ReviewForm is the form using for the review creation.
    """
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body',]


class FollowUsersForm(forms.ModelForm):
    """
        Class FollowUsersForm is the form using for the relation between two user.
    """
    class Meta:
        model = models.UserFollows
        fields = ['followed_user',]
