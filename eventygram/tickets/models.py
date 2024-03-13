from eventygram.tickets.choices import PAYMENT_STATUS_CHOICES
from django.db.models.signals import post_save, post_delete
from eventygram.accounts.models import UserProfile
from django.core.exceptions import ValidationError
from eventygram.events.models import Event
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
import uuid
import os


class Ticket(models.Model):
    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
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
    )

    def clean(self):
        super().clean()
        if self.purchase_date and self.purchase_date > timezone.now():
            raise ValidationError("Purchase date cannot be in the future.")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.event.price
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


@receiver(post_delete, sender=UserProfile)
def delete_profile_picture(sender, instance, **kwargs):
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)


@receiver(post_delete, sender=Event)
def delete_event_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
