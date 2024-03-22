import random
from django.shortcuts import render, get_object_or_404, redirect
from eventygram.tickets.forms import CreateTicketForm, BuyTicketsForm
from eventygram.accounts.models import Profile
from eventygram.events.models import Event
from django.views import View

from eventygram.tickets.models import Ticket


class CreateTicketView(View):
    def get(self, request, event_id):
        if request.user.is_authenticated:
            form = CreateTicketForm()
            event = Event.objects.get(id=event_id)

            context = {
                'form': form,
                'event': event,
            }

            return render(request, 'tickets/ticket_create.html', context)

        else:
            return redirect('login')

    def post(self, request, event_id):
        if request.user.is_authenticated:
            form = CreateTicketForm(request.POST)

            if form.is_valid():
                event = Event.objects.get(id=event_id)
                price = event.price
                num_tickets = form.cleaned_data['num_tickets']

                event.generate_tickets(
                    num_tickets=num_tickets,
                    ticket_price=price,
                )

                event.available_tickets += num_tickets
                event.ticket_sales = True
                event.save()

                return redirect('successful_ticket_creation', event_id=event_id)
            else:
                context = {'form': form, 'event_id': event_id}
                return render(request, 'tickets/ticket_create.html', context)
        else:
            return redirect('login')


class MyTicketsView(View):
    def get(self, request, pk):
        user = get_object_or_404(Profile, pk=pk)
        tickets = user.ticket_set.all()

        context = {
            'user': user,
            'tickets': tickets,
        }

        return render(request, 'accounts/my_tickets.html', context)


def ticket_details(request):
    context = {}

    return render(request, 'tickets/ticket_details.html', context)


def successful_ticket_creation(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event
    }

    return render(request, 'tickets/successful_ticket_creation.html', context)


def buy_tickets(request, event_id):
    event = Event.objects.get(id=event_id)
    form = BuyTicketsForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        num_tickets = form.cleaned_data['num_tickets']
        ticket_price = event.price
        profile = get_object_or_404(Profile, pk=request.user.pk)
        balance = profile.balance

        if balance < num_tickets * ticket_price:
            pass
        else:
            available_tickets = Ticket.objects.filter(event=event, payment_status='Available')

            if available_tickets.count() < num_tickets:
                pass
            else:
                selected_tickets = random.sample(list(available_tickets), num_tickets)

                for ticket in selected_tickets:
                    ticket.owner = profile
                    ticket.payment_status = 'Paid'
                    ticket.save()

                profile.deduct_balance(num_tickets * ticket_price)
                event.available_tickets -= num_tickets
                event.save()
                event.creator.add_balance(num_tickets * ticket_price)

            return redirect('ticket_purchase_successful', event_id=event.pk)

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'tickets/buy_tickets.html', context)


def ticket_purchase_successful(request, event_id):
    context = {}

    return render(request, 'tickets/tickets_purchase_successful.html', context)
