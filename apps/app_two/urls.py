from django.urls import path
from .views import ProductAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'v1/product/', ProductAPIView.as_view(), name='Product')
]

urlpatterns = format_suffix_patterns(urlpatterns)