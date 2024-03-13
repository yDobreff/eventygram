# Generated by Django 5.0.2 on 2024-03-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_number',
        ),
        migrations.AddField(
            model_name='ticket',
            name='number',
            field=models.CharField(default='57926C7670', max_length=50, unique=True),
        ),
    ]
