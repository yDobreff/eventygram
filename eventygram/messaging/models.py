from eventygram.accounts.models import UserProfile
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='sent_messages',
    )

    receiver = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='received_messages',
    )

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    @classmethod
    def send_message(cls, sender, receiver, subject, message_content):
        message = cls.objects.create(
            sender=sender,
            receiver=receiver,
            subject=subject,
            message=message_content
        )
        return message

    @classmethod
    def get_received_messages(cls, user):
        return cls.objects.filter(receiver=user)

    @classmethod
    def get_unread_messages(cls, user):
        return cls.objects.filter(receiver=user, is_read=False)
