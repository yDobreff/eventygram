from django.shortcuts import render, get_object_or_404, redirect
from eventygram.messaging.forms import MessageForm
from eventygram.messaging.models import Message
from eventygram.accounts.models import Profile
from django.contrib.auth import get_user_model


def inbox(request, pk):
    user = get_object_or_404(Profile, pk=pk)

    received_messages = Message.objects.filter(receiver=request.user)
    sent_messages = Message.objects.filter(sender=request.user)

    context = {
        'received_messages': received_messages,
        'sent_messages': sent_messages,
        'user': user,
    }

    return render(request, 'messaging/inbox.html', context)


def send_message(request, pk):
    profile_model = get_user_model()
    profile = get_object_or_404(profile_model, pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()

            return redirect('message_sent_successfully', pk=profile.pk)
    else:
        form = MessageForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'messaging/send_message.html', context)


def message_sent_successfully(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    context = {
        'profile': profile
    }

    return render(request, 'messaging/message_sent_successfully.html', context)


def delete_message(request, profile_pk, message_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    message = get_object_or_404(Message, pk=message_pk)

    context = {
        'profile': profile,
        'message': message,
    }

    return render(request, 'messaging/delete_message.html', context)
