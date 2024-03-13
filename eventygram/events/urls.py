from django.urls import path
from eventygram.events import views
from eventygram.events.views import EventsCatalogueView, EventCreateView

urlpatterns = [
    path('catalogue/', EventsCatalogueView.as_view(), name='events_catalogue'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('create/successful/<int:pk>/', views.successful_event_registration, name='successful_event_registration'),
    path('<int:pk>/details/', views.event_details, name='event_details'),
    path('<int:pk>/update/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('<int:pk>/my_events/', views.my_events, name='my_events')
]
