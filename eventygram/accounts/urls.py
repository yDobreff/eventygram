from eventygram.accounts.views import RegisterUserView, LoginUserView, UpdateUserView
from eventygram.accounts import views
from django.urls import path


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register/successful/<int:pk>/', views.successful_registration, name='successful_registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('login/successful/<int:pk>/', views.successful_login, name='successful_login'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:pk>/details/', views.profile_details, name='profile_details'),
    path('<int:pk>/edit/', UpdateUserView.as_view(), name='profile_update'),
]
