from eventygram.events.forms import EventCreationForm, EventUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from eventygram.events.models import Event, Like, Comment
from django.views import View


class EventsCatalogueView(View):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()

        context = {
            'events': events,
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
            return redirect('successful_course_registration', pk=event.pk)
        else:
            context = {
                'form': form
            }

        return render(request, 'events/event_create.html', context)


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    user_liked_event = None
    comments = Comment.objects.all()

    if request.user.is_authenticated:
        user_liked_event = Like.objects.filter(profile=request.user, event=event).exists()

    context = {
        'event': event,
        'user_liked_event': user_liked_event,
        'comments': comments,
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
            Comment.objects.create(user=request.user, event=event, content=content)
            return redirect('event_details', pk=pk)

    context = {
        'event': event,
    }

    return render(request, 'events/leave_comment.html', context)
