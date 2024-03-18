from django.urls import path
from eventygram.messaging import views

urlpatterns = [
    path('<int:pk>/inbox/', views.inbox, name='inbox'),
    path('<int:pk>/send_message/', views.send_message, name='send_message'),
    path('<int:pk>/sent/', views.message_sent_successfully, name='message_sent_successfully'),
    path('<int:profile_pk>/message/<int:message_pk>', views.delete_message, name='delete_message'),
]