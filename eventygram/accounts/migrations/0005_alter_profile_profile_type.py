# Generated by Django 5.0.2 on 2024-03-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('User', 'User'), ('Company', 'Company'), ('Organization', 'Organization'), ('Oligofren', 'Oligofren')], max_length=20),
        ),
    ]