from django.views.generic import TemplateView

from eventygram.events.views import EventsCatalogueView, EventCreateView
from eventygram.accounts import views as accounts_views
from eventygram.events import views
from django.urls import path

urlpatterns = [
    path('catalogue/', EventsCatalogueView.as_view(), name='events_catalogue'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('create/successful/<int:pk>/', views.successful_event_registration, name='successful_event_registration'),
    path('<int:pk>/details/', views.event_details, name='event_details'),
    path('<int:pk>/update/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('<int:pk>/my_events/', accounts_views.profile_events, name='user_events'),
    path('<int:pk>/like', views.like_event, name='like_event'),
    path('<int:pk>/unlike', views.unlike_event, name='unlike_event'),
    path('<int:pk>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('<int:pk>/participate/', views.participate_event, name='participate_event'),
    path('<int:pk>/withdraw_event_participation/', views.withdraw_event_participation, name='withdraw_event_participation'),
]
