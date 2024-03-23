from eventygram.courses.views import CoursesCatalogueView, CourseCreateView
from eventygram.accounts import views as accounts_views
from eventygram.courses import views
from django.urls import path

urlpatterns = [
    path('catalogue/', CoursesCatalogueView.as_view(), name='courses_catalogue'),
    path('<int:pk>/topic/', views.topic_view, name='topic_view'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('create/successful/<int:pk>/', views.successful_course_registration, name='successful_course_registration'),
    path('<int:pk>/my_courses/', accounts_views.profile_courses, name='my_courses'),
    path('<int:pk>/details/', views.course_details, name='course_details'),
    path('<int:pk>/update/', views.course_update, name='course_update'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),
    # path('<int:pk>/my_events/', accounts_views.profile_events, name='user_events'),
    # path('<int:pk>/like', views.like_event, name='like_event'),
    # path('<int:pk>/unlike', views.unlike_event, name='unlike_event'),
    # path('<int:pk>/leave_comment/', views.leave_comment, name='leave_comment'),
]
