from eventygram.tickets.views import CreateTicketView, MyTicketsView
from eventygram.tickets import views
from django.urls import path

urlpatterns = [
    path('create/', CreateTicketView.as_view(), name='ticket_create'),
    path('<int:pk>/my_tickets/', MyTicketsView.as_view(), name='my_tickets'),
    path('<int:pk>/details/', views.ticket_details, name='ticket_details'),
]