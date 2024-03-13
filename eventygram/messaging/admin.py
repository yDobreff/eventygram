from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'subject', 'timestamp', 'is_read']
    list_filter = ['sender', 'receiver', 'is_read']
    search_fields = ['subject', 'message']
    readonly_fields = ['timestamp']
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected messages marked as read.")

    mark_as_read.short_description = "Mark selected messages as read"