# Generated by Django 5.0.2 on 2024-03-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_alter_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.CharField(default='1AF0B1A540', max_length=50, unique=True),
        ),
    ]
