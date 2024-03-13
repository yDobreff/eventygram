from django.contrib import admin
from eventygram.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'venue',
        'start_time',
        'end_time',
        'type',
        'available_tickets',
        'get_participants_count',
        'status',
        'price',
    ]
    list_filter = ['start_time', 'venue', 'type', 'price', 'status']
    search_fields = ['name', 'location']

    def get_participants_count(self, obj):
        return obj.participants.count()

    get_participants_count.short_description = 'Participants'

