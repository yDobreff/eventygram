from django.shortcuts import render, get_object_or_404, redirect
from eventygram.tickets.forms import CreateTicketForm
from eventygram.accounts.models import Profile
from eventygram.events.models import Event
from django.views import View


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
                event.save()

                return redirect('successful_ticket_creation')
            else:
                context = {'form': form, 'event_id': event_id}
                return render(request, 'tickets/ticket_create.html', context)
        else:
            return redirect('login')


class MyTicketsView(View):
    def get(self, request, pk):
        user = get_object_or_404(Profile, pk=pk)
        context = {
            'user': user
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
