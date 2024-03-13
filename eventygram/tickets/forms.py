from eventygram.tickets.models import Ticket
from django.views import View


class CreateTicketView(View):
    class Meta:
        model = Ticket
        fields = '__all__'
