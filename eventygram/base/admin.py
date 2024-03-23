from eventygram.base.models import ContactHistory
from django.contrib import admin


@admin.register(ContactHistory)
class ContactHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'subject',
        'message',
    ]