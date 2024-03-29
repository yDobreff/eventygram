from eventygram.events.validators import validate_start_time
from eventygram.events.helpers import event_pic_path
from eventygram.accounts.models import Profile
from eventygram.events import choices
from django.db import models
import os


class Event(models.Model):
    creator = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='event_creator',
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    region = models.CharField(
        max_length=100,
        choices=choices.REGIONS,
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=150,
    )

    image = models.ImageField(
        upload_to=event_pic_path,
        blank=True,
        null=True,
    )

    start_time = models.DateTimeField(
        validators=([validate_start_time])
    )

    end_time = models.DateTimeField(
    )

    type = models.CharField(
        max_length=100,
        choices=choices.EVENT_TYPES,
    )

    participants = models.ManyToManyField(
        Profile,
        blank=True,
        related_name='participants'
    )

    status = models.CharField(
        choices=choices.EVENT_STATUS,
        null=True,
        blank=True,
        default='Active',
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )

    likes = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Event.objects.get(pk=self.pk)
            except Event.DoesNotExist:
                pass
            else:
                if old_instance.image != self.image and old_instance.image:
                    os.remove(old_instance.image.path)
        super().save(*args, **kwargs)

    def get_price_display(self):
        if self.price == 0.0:
            return "Free"
        else:
            return "${:.2f}".format(self.price)

    def tickets_count(self):
        available_tickets = self.ticket_set.filter(payment_status='Available').count()

        if available_tickets == 0:
            return "No tickets available"
        else:
            return available_tickets


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    content = models.TextField()

    date_posted = models.DateTimeField(
        auto_now_add=True
    )
