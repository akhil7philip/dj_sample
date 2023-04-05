from django.urls import re_path
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.views import (
    LoginView as login, LogoutView as logout
)
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    re_path(r'^$', views.view_profile),
    re_path(r'^login/$', login.as_view(template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', logout.as_view(template_name='accounts/logout.html'), name='logout'),
    re_path(r'^profile/$', views.view_profile, name='view_profile'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    re_path(r'^profile/edit/$', views.edit_profile, name='edit_profile')
]
