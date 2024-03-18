from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_purchase_date_not_future(value):
    if value > timezone.now():
        raise ValidationError("Purchase date cannot be in the future.")
