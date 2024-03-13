# Generated by Django 5.0.2 on 2024-03-09 13:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_rename_start_date_event_end_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Failed', 'Failed')], max_length=50)),
                ('ticket_number', models.CharField(default='00A096DD9E', max_length=50, unique=True)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('ticket_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]