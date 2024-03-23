from eventygram.tickets.validators import validate_purchase_date_not_future
from eventygram.tickets.choices import PAYMENT_STATUS
from eventygram.accounts.models import Profile
from eventygram.events.models import Event
from django.db import models


class Ticket(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        related_name='tickets'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    payment_status = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS,
    )

    number = models.CharField(
        max_length=50,
        unique=True,
        default=None,
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
