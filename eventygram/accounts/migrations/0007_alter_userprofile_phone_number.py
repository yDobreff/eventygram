# Generated by Django 5.0.2 on 2024-03-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, max_length=10, null=True),
        ),
    ]