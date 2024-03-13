from eventygram.events.forms import EventCreationForm, EventUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from eventygram.accounts.models import UserProfile
from eventygram.events.models import Event
from django.views import View


class EventsCatalogueView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'events/events_catalogue.html', context)


class EventCreateView(View):
    def get(self, request):
        form = EventCreationForm()

        context = {
            'form': form
        }
        return render(request, 'events/event_create.html', context)

    def post(self, request):
        form = EventCreationForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            form.save_m2m()
            return redirect('successful_event_registration', pk=event.pk)
        else:
            context = {
                'form': form
            }

        return render(request, 'events/event_create.html', context)


def successful_event_registration(request, pk):
    event = get_object_or_404(Event, pk=pk)

    context = {
        'event': event
    }

    return render(request, 'events/successful_event_registration.html', context)


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)

    context = {
        'event': event,
    }

    return render(request, 'events/event_details.html', context)


def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventUpdateForm(instance=event)

    if request.method == "POST":
        form = EventUpdateForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_details', pk=event.pk)

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'events/event_update.html', context)


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        event.delete()
        return redirect('events_catalogue')

    context = {
        'event': event,
    }

    return render(request, 'events/event_delete.html', context)


def my_events(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    events = user.event_set.all()

    context = {
        'events': events,
    }

    return render(request, 'events/../../templates/accounts/my_events.html', context)
