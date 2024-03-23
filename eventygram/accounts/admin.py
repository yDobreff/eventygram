from eventygram.accounts.models import Profile, ProfileSubscriber
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    list_display = [
        'username',
        'email',
        'profile_type',
        'is_staff',
        'is_active',
        'date_joined'
    ]

    list_filter = [
        'profile_type',
        'is_staff',
        'is_active',
    ]


@admin.register(ProfileSubscriber)
class ProfileSubscriberAdmin(admin.ModelAdmin):
    list_display = [
        'subscriber',
        'subscribed_to',
        'subscribed_at'
    ]
