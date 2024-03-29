from eventygram.base.forms import ContactForm, SearchForm
from eventygram.base.models import ContactHistory
from eventygram.accounts.models import Profile
from django.shortcuts import render, redirect

from eventygram.courses.models import Course
from eventygram.events.models import Event
from django.core.mail import send_mail
from eventygram import settings
from django.views import View
import random


def index(request):
    events = random.sample(list(Event.objects.all()), 3)
    event_one = events[0]
    event_two = events[1]
    event_three = events[2]

    context = {
        'event_one': event_one,
        'event_two': event_two,
        'event_three': event_three,
    }

    return render(request, 'base/index.html', context)


def about(request):
    return render(request, 'base/about.html')


class ContactView(View):
    def get(self, request):
        form = ContactForm()

        return render(request, 'base/contacts.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            message_content = f'From: {username}\n\nMessage: {message}'
            sender_email = form.cleaned_data['email']
            receiver_email = settings.EMAIL_HOST_USER

            contact_history = ContactHistory.objects.create(
                username=username,
                email=sender_email,
                subject=subject,
                message=message,
            )

            contact_history.save()

            send_mail(
                subject,
                message_content,
                sender_email,
                [receiver_email],
                fail_silently=False
            )

            return redirect('successful_message')

        return render(request, 'base/contacts.html', {'form': form})


def profile(request):
    user = request.user

    return redirect('profile_details', pk=user.pk)


def successful_message(request):
    return render(request, 'base/successful_message.html')


def search_result(request):
    form = SearchForm(request.GET)
    search_results = None
    if form.is_valid():
        query = form.cleaned_data['query']
        search_results = {
            'events': Event.objects.filter(title__icontains=query, status='Active'),
            'profiles': Profile.objects.filter(username__icontains=query, is_private=False),
            'courses': Course.objects.filter(title__icontains=query),
        }

    return render(request, 'base/search_results.html', {'search_results': search_results})
