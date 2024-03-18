from django.urls import path
from eventygram.base import views
from eventygram.base.views import ContactView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('contacts/successful_message/', views.successful_message, name='successful_message'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_result, name='search_results'),
]
