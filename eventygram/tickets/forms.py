from django import forms


class CreateTicketForm(forms.Form):
    num_tickets = forms.IntegerField()
