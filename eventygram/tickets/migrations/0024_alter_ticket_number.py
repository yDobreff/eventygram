# Generated by Django 5.0.2 on 2024-03-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0023_alter_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.CharField(default='0E2C1F1BB9', max_length=50, unique=True),
        ),
    ]