from django.shortcuts import render, get_object_or_404, redirect
from eventygram.accounts.models import UserProfile
from django.views import View


class CreateTicketView(View):
    def post(self, request):
        if request.user.is_authenticated:
            context = {}
            return render(request, 'tickets/ticket_create.html', context)

        return redirect('my_tickets')


class MyTicketsView(View):
    def get(self, request, pk):
        user = get_object_or_404(UserProfile, pk=pk)
        context = {
            'user': user
        }

        return render(request, 'tickets/../../templates/accounts/my_tickets.html', context)


def ticket_details(request):
    context = {}

    return render(request, 'tickets/ticket_details.html', context)
