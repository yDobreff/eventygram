from eventygram.events.choices import EVENT_TYPE_CHOICES, EVENT_STATUS_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from eventygram.events.validators import validate_start_time
from eventygram.accounts.models import UserProfile
from eventygram import settings
from django.db import models
import os


def event_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}_pic.{ext}"
    return os.path.join(settings.MEDIA_ROOT, '_pics', filename)


class Event(models.Model):
    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    venue = models.CharField(
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
        choices=EVENT_TYPE_CHOICES,
    )

    available_tickets = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
    )

    participants = models.ManyToManyField(
        UserProfile,
        blank=True
    )

    status = models.CharField(
        choices=EVENT_STATUS_CHOICES,
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
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


class Review(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
    )

    comment = models.TextField()

    date_posted = models.DateTimeField(
        auto_now_add=True
    )


class Comment(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    content = models.TextField()

    date_posted = models.DateTimeField(
        auto_now_add=True
    )
