from eventygram.tickets.views import CreateTicketView, MyTicketsView
from eventygram.tickets import views
from django.urls import path

urlpatterns = [
    path('create/<int:event_id>/', CreateTicketView.as_view(), name='ticket_create'),
    path('<int:pk>/my_tickets/', MyTicketsView.as_view(), name='my_tickets'),
    path('<int:pk>/details/', views.ticket_details, name='ticket_details'),
    path('successful_ticket_creation/<int:event_id>/', views.successful_ticket_creation, name='successful_ticket_creation')
]