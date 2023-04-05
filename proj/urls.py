"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
]


schema_view = get_swagger_view(title="Proj Swagger API Documentation")
urlpatterns = [
                re_path(r'^$', views.login_redirect, name='login_redirect'),
                re_path(r'^admin/', admin.site.urls),
                re_path(r'^app_one/', include(('proj.apps.app_one.urls', 'app_one'), namespace='app_one')),
                re_path(r'^app_one/', include(('proj.apps.app_one.urls', 'app_one'), namespace='app_one')),
                re_path(r'^accounts/', include(('proj.apps.accounts.urls', 'accounts'), namespace='accounts'))
                ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
