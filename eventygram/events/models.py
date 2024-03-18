from eventygram.events.choices import EVENT_TYPE_CHOICES, EVENT_STATUS_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from eventygram.events.validators import validate_start_time
from eventygram.events.helpers import event_pic_path
from eventygram.accounts.models import Profile
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

    is_private = models.BooleanField(
        default=False,
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

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
        choices=EVENT_TYPE_CHOICES,
    )

    tickets_sales = models.BooleanField(
        default=False
    )

    available_tickets = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
    )

    participants = models.ManyToManyField(
        Profile,
        blank=True
    )

    status = models.CharField(
        choices=EVENT_STATUS_CHOICES,
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


class EventTaskManager(Event):
    class Meta:
        proxy = True

    def get_price_display(self):
        if self.price == 0.0:
            return "Free"
        else:
            return "${:.2f}".format(self.price)

    def generate_tickets(self, num_tickets, ticket_price):
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be greater than 0.")

        from eventygram.tickets.models import Ticket

        for _ in range(num_tickets):
            Ticket.objects.create(
                owner=None,
                event=self,
                payment_status='Available',
                price=ticket_price,
            )

        self.tickets_sales = True
        self.price = ticket_price
        self.save()


class Review(models.Model):
    user = models.ForeignKey(
        Profile,
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
        Profile,
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
