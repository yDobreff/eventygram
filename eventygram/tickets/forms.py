from django.core.validators import MinValueValidator
from django import forms


class BaseTicketsForm(forms.Form):
    num_tickets = forms.IntegerField(
        validators=[MinValueValidator(-1)],
        label='Number of Tickets',
    )


class CreateTicketForm(BaseTicketsForm):
    pass


class BuyTicketsForm(BaseTicketsForm):
    pass
