# Generated by Django 5.0.2 on 2024-03-18 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_event_is_private_alter_event_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventTaskManager',
        ),
    ]
