# Generated by Django 5.0.2 on 2024-03-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.CharField(default='38D1B95638', max_length=50, unique=True),
        ),
    ]