from eventygram.accounts.views import LoginProfileView, CreateProfileView, UpdateProfileView
from eventygram.accounts import views
from django.urls import path

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='profile_register'),
    path('register/successful/<int:pk>/', views.successful_registration, name='successful_registration'),
    path('login/', LoginProfileView.as_view(), name='profile_login'),
    path('login/successful/<int:pk>/', views.successful_login, name='successful_login'),
    path('logout/', views.logout_profile, name='profile_logout'),
    path('<int:pk>/details/', views.profile_details, name='profile_details'),
    path('<int:pk>/edit/', UpdateProfileView.as_view(), name='profile_update'),
    path('<int:pk>/add_balance/', views.add_balance, name='add_balance'),
    path('<int:pk>/subscribe/', views.subscribe_profile, name='subscribe_profile'),
    path('<int:pk>/unsubscribe/', views.unsubscribe_profile, name='unsubscribe_profile'),
    path('<int:pk>/change_password/', views.change_password, name='change_password'),
    path('<int:pk>/change_password/successful/', views.successful_password, name='successful_password'),
]
