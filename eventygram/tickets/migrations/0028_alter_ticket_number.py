# Generated by Django 5.0.2 on 2024-03-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0027_alter_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.CharField(default='84B4F07C28', max_length=50, unique=True),
        ),
    ]