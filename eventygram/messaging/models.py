from eventygram.accounts.models import Profile
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='sent_messages',
    )

    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='received_messages',
    )

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    sent_on = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def send_message(self, sender, receiver, subject, message_content):
        message = self.objects.create(
            sender=sender,
            receiver=receiver,
            subject=subject,
            message=message_content
        )
        return message
