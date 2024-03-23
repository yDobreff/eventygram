from eventygram.messaging.models import Message
from django.forms import ModelForm


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'receiver',
            'subject',
            'message',
        ]