from django.shortcuts import render, get_object_or_404, redirect
from ..accounts.models import UserProfile
from .forms import MessageForm
from .models import Message


def inbox(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)

    received_messages = Message.objects.filter(receiver=request.user)
    sent_messages = Message.objects.filter(sender=request.user)

    context = {
        'received_messages': received_messages,
        'sent_messages': sent_messages,
        'user': user,
    }

    return render(request, 'messaging/inbox.html', context)


def send_message(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_sent_successfully', pk=user.pk)
    else:
        form = MessageForm()

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'messaging/send_message.html', context)


def message_sent_successfully(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)

    context = {
        'user': user
    }

    return render(request, 'messaging/message_sent_successfully.html', context)


def delete_message(request, user_pk, message_pk):
    user = get_object_or_404(UserProfile, pk=user_pk)
    message = get_object_or_404(Message, pk=message_pk)

    context = {
        'user': user,
        'message': message,
    }

    return render(request, 'messaging/delete_message.html', context)