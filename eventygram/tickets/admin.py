from eventygram.tickets.models import Ticket
from django.contrib import admin


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'event',
        'payment_status',
        'number',
        'purchase_date',
    ]
    list_filter = [
        'owner',
        'event',
    ]

    search_fields = [
        'event',
        'type',
    ]
