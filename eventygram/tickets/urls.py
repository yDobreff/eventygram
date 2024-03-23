from django.views.generic import TemplateView

from eventygram.tickets.views import CreateTicketView, MyTicketsView
from eventygram.tickets import views
from django.urls import path

urlpatterns = [
    path('create/<int:event_id>/', CreateTicketView.as_view(), name='ticket_create'),
    path('<int:pk>/my_tickets/', MyTicketsView.as_view(), name='my_tickets'),
    path('<int:pk>/details/', views.ticket_details, name='ticket_details'),
    path('successful_ticket_creation/<int:event_id>/', views.successful_ticket_creation,
         name='successful_ticket_creation'),
    path('<int:event_id>/buy_tickets/', views.buy_tickets, name='buy_tickets'),
    path('<int:event_id>/ticket_purchase_successful/', TemplateView.as_view(
        template_name='tickets/tickets_purchase_successful.html'), name='ticket_purchase_successful'),
]