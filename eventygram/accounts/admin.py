from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from eventygram.accounts.models import Profile


@admin.register(Profile)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
