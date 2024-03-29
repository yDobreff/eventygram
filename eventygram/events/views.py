from eventygram.events.forms import EventCreationForm, EventUpdateForm, EventFilterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from eventygram.events.models import Event, Like, Comment
from eventygram.events.helpers import get_price_range
from eventygram.tickets.models import Ticket
from django.views import View


class EventsCatalogueView(View):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        form = EventFilterForm(request.GET)

        if form.is_valid():
            event_type_dropdown = request.GET.get('type')
            event_type_filter = form.cleaned_data.get('type')

            if event_type_dropdown:
                events = events.filter(type=event_type_dropdown)
            elif event_type_filter:
                events = events.filter(type=event_type_filter)

            region = form.cleaned_data.get('region')
            price_range = form.cleaned_data.get('price_range')

            if region:
                events = events.filter(region=region)
            if price_range:
                min_price, max_price = get_price_range(price_range)
                if min_price is not None and max_price is not None:
                    events = events.filter(price__gte=min_price, price__lte=max_price)

        sort_by = request.GET.get('sort_by')
        if sort_by == 'likes':
            events = events.order_by('-likes')
        elif sort_by == 'price':
            events = events.order_by('price')

        context = {
            'events': events,
            'form': form,
        }

        return render(request, 'events/events_catalogue.html', context)


class EventCreateView(LoginRequiredMixin, View):
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
            event.creator = request.user
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
        'event': event,
    }

    return render(request, 'events/successful_event_registration.html', context)


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    user_liked_event = None
    user_participated = None
    user_has_ticket = None
    comments = Comment.objects.filter(event_id=event.pk)

    if request.user.is_authenticated:
        user_liked_event = Like.objects.filter(profile=request.user, event=event).exists()
        user_participated = event.participants.filter(pk=request.user.pk).exists()
        user_has_ticket = Ticket.objects.filter(owner=request.user, event=event).exists()

    context = {
        'event': event,
        'user_liked_event': user_liked_event,
        'user_participated': user_participated,
        'comments': comments,
        'user_has_ticket': user_has_ticket,
    }

    return render(request, 'events/event_details.html', context)


@login_required
def like_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if not Like.objects.filter(profile=request.user, event=event).exists():
        Like.objects.create(profile=request.user, event=event)
        event.likes += 1
        event.save()

    return redirect('event_details', pk=event.pk)


@login_required
def unlike_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    like = Like.objects.filter(profile=request.user, event=event).first()
    if like:
        like.delete()
        event.likes -= 1
        event.save()
    return redirect('event_details', pk=event.pk)


@login_required
def participate_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if not event.participants.filter(pk=request.user.pk).exists():
        event.participants.add(request.user)
        event.save()

        user_tickets = Ticket.objects.filter(owner=request.user, event=event)
        if user_tickets.count() > 0:
            user_tickets.first().delete()

    return redirect('event_details', pk=event.pk)


@login_required
def withdraw_event_participation(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if event.participants.filter(pk=request.user.pk).exists():
        event.participants.remove(request.user)
        event.save()

        Ticket.objects.create(owner=request.user, event=event)

    return redirect('event_details', pk=event.pk)


@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventUpdateForm(instance=event)

    if request.user != event.creator:
        return redirect('events_catalogue')

    if request.method == "POST":
        form = EventUpdateForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_details', pk=event.pk)

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'events/event_update.html', context)


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        event.delete()
        return redirect('events_catalogue')

    context = {
        'event': event,
    }

    return render(request, 'events/event_delete.html', context)


@login_required
def leave_comment(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Comment.objects.create(profile=request.user, event=event, content=content)
            return redirect('event_details', pk=pk)

    context = {
        'event': event,
    }

    return render(request, 'events/leave_comment.html', context)
