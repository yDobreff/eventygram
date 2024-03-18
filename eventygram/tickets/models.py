from eventygram.tickets.validators import validate_purchase_date_not_future
from eventygram.tickets.choices import PAYMENT_STATUS_CHOICES
from django.db.models.signals import post_save, post_delete
from eventygram.accounts.models import Profile
from eventygram.events.models import Event
from django.dispatch import receiver
from django.db import models
import uuid
import os


class Ticket(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    payment_status = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_CHOICES,
    )

    number = models.CharField(
        max_length=50,
        unique=True,
        default=uuid.uuid4().hex[:10].upper(),
    )

    purchase_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        validators=[
            validate_purchase_date_not_future
        ],
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            unique_number_generated = False
            while not unique_number_generated:
                generated_number = uuid.uuid4().hex[:10].upper()
                if not Ticket.objects.filter(number=generated_number).exists():
                    unique_number_generated = True
                    self.number = generated_number

            if self.owner:
                self.owner.deduct_balance(self.price)

            if self.event.available_tickets > 0:
                self.event.available_tickets -= 1
                self.event.save()

        super().save(*args, **kwargs)


@receiver(post_save, sender=Ticket)
def decrease_available_tickets(sender, instance, created, **kwargs):
    if created and instance.event.available_tickets > 0:
        instance.event.available_tickets -= 1
        instance.event.save()


@receiver(post_delete, sender=Profile)
def delete_profile_picture(sender, instance, **kwargs):
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)


@receiver(post_delete, sender=Event)
def delete_event_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
