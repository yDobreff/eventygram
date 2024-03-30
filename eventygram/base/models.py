from django.db import models


class ContactHistory(models.Model):
    username = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=150,
    )

    message = models.CharField()

    class Meta:
        verbose_name_plural = "Contact history"
