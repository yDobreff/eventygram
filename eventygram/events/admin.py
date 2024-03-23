from eventygram.events.models import Event, Like, Comment
from django.contrib import admin


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'location',
        'start_time',
        'end_time',
        'type',
        'status',
        'price',
    ]
    list_filter = [
        'start_time',
        'location',
        'type',
        'price',
        'status',
    ]
    search_fields = ['name', 'location']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'event',
        'created_at',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'event',
        'content',
        'date_posted',
    ]