from django.forms import ModelForm
from eventygram.messaging.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'receiver',
            'subject',
            'message'
        ]