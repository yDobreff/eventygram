from django.contrib.auth.models import AbstractUser, Group, Permission
from eventygram.accounts.helpers import profile_pic_path
from eventygram.accounts.validators import phone_regex
from django.core.exceptions import ValidationError
from eventygram.accounts import choices
from django.db import models
from datetime import date
import os


class Profile(AbstractUser):
    profile_type = models.CharField(
        max_length=20,
        choices=choices.PROFILE_TYPES,
        null=False,
        blank=False
    )

    is_private = models.BooleanField(
        default=False,
    )

    # FIELDS FOR ALL PROFILE TYPES

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    phone_number = models.CharField(
        max_length=17,
        validators=[phone_regex],
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to=profile_pic_path,
        blank=True,
        null=True
    )

    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    # FIELDS FOR INDIVIDUAL USER

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    bio = models.TextField(
        max_length=250,
        blank=True,
        null=True,
    )

    # FIELDS FOR COMPANY

    industry = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    address = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=250,
        blank=True,
        null=True,
    )

    # FIELDS FOR ORGANIZATION

    type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    mission = models.TextField(
        max_length=250,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Profile.objects.get(pk=self.pk)
            except self.DoesNotExist:
                pass
            else:
                if old_instance.profile_picture != self.profile_picture:
                    if old_instance.profile_picture:
                        os.remove(old_instance.profile_picture.path)

        super().save(*args, **kwargs)

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return age
        return None

    def add_balance(self, amount):
        self.balance += amount
        self.save()

    def deduct_balance(self, amount):
        if self.balance < amount:
            raise ValidationError("Insufficient balance.")
        self.balance -= amount
        self.save()


class ProfileSubscriber(models.Model):
    subscriber = models.ForeignKey(
        Profile,
        related_name='subscriptions',
        on_delete=models.CASCADE,
    )

    subscribed_to = models.ForeignKey(
        Profile,
        related_name='subscribers',
        on_delete=models.CASCADE,
    )

    subscribed_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = [
            'subscriber',
            'subscribed_to',
        ]
