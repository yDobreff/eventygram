from eventygram.messaging.models import Message
from django.contrib import admin


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'sender',
        'receiver',
        'subject',
        'sent_on',
        'is_read',
    ]
    list_filter = [
        'sender',
        'receiver',
        'is_read',
    ]
    search_fields = [
        'subject',
        'message',
    ]
    readonly_fields = [
        'sent_on',
    ]
