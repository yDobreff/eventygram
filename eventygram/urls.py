"""
URL configuration for eventygram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from eventygram import settings

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('eventygram.base.urls')),
    path('profile/', include('eventygram.accounts.urls')),
    path('events/', include('eventygram.events.urls')),
    path('tickets/', include('eventygram.tickets.urls')),
    path('messages/', include('eventygram.messaging.urls')),
    path('courses/', include('eventygram.courses.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
