from django.core.validators import MinValueValidator
from django import forms

from eventygram.tickets.models import Ticket


class CreateTicketForm(forms.Form):
    num_tickets = forms.IntegerField(
        validators=[MinValueValidator(-1)],
        label='Number of Tickets',
    )


class BuyTicketsForm(forms.Form):
    num_tickets = forms.IntegerField(
        validators=[MinValueValidator(-1)],
        label='Number of Tickets',
    )