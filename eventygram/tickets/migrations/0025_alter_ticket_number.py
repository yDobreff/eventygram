# Generated by Django 5.0.2 on 2024-03-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0024_alter_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.CharField(default='8002A65641', max_length=50, unique=True),
        ),
    ]
