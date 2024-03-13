# Generated by Django 5.0.2 on 2024-03-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateField()),
                ('event_type', models.CharField(choices=[('Concerts', 'Concerts'), ('Sports', 'Sports'), ('Cultural', 'Cultural'), ('Educational', 'Educational'), ('Community', 'Community'), ('Political', 'Political'), ('Travel', 'Travel'), ('Entertainment', 'Entertainment')], max_length=100)),
                ('is_active', models.BooleanField()),
                ('available_tickets', models.PositiveIntegerField(blank=True, null=True)),
                ('participants', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
