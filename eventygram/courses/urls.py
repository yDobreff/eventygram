from eventygram.courses.views import CoursesCatalogueView, CourseCreateView
from eventygram.accounts import views as accounts_views
from django.views.generic import TemplateView
from eventygram.courses import views
from django.urls import path

urlpatterns = [
    path('catalogue/', CoursesCatalogueView.as_view(), name='courses_catalogue'),
    path('<int:pk>/topic/', views.topic_view, name='topic_view'),
    path('create/', CourseCreateView.as_view(), name='create_course'),
    path('create/successful/<int:pk>/', TemplateView.as_view(
        template_name='courses/successful_course_registration.html'), name='successful_course_registration'),
    path('<int:pk>/my_courses/', accounts_views.profile_courses, name='my_courses'),
    path('<int:pk>/details/', views.course_details, name='course_details'),


    # path('<int:pk>/update/', views.event_update, name='event_update'),
    # path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    # path('<int:pk>/my_events/', accounts_views.profile_events, name='user_events'),
    # path('<int:pk>/like', views.like_event, name='like_event'),
    # path('<int:pk>/unlike', views.unlike_event, name='unlike_event'),
    # path('<int:pk>/leave_comment/', views.leave_comment, name='leave_comment'),
]
