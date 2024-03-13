from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from eventygram import settings
from django.db import models
import os


def profile_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}_profile_pic.{ext}"
    return os.path.join(settings.MEDIA_ROOT, 'profile_pics', filename)


class UserProfile(AbstractUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    bio = models.TextField(
        max_length=250,
        blank=True,
        null=True,
    )
    phone_number = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=200,
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
    age = models.IntegerField(
        validators=[MaxValueValidator(150), MinValueValidator(0)],
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = UserProfile.objects.get(pk=self.pk)
            except UserProfile.DoesNotExist:
                pass
            else:
                if old_instance.profile_picture != self.profile_picture:
                    if old_instance.profile_picture:
                        os.remove(old_instance.profile_picture.path)
        super().save(*args, **kwargs)

    # Add balance to user
    def add_balance(self, amount):
        self.balance += amount
        self.save()

    # Deduct balance of user
    def deduct_balance(self, amount):
        if self.balance < amount:
            raise ValidationError("Insufficient balance.")
        self.balance -= amount
        self.save()


