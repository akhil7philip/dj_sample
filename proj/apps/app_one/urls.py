from django.urls import path,include
from .views import SalesSummaryAPIView, SummerSalesAPIView, FallSalesAPIView, WinterSalesAPIView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
    
router = routers.DefaultRouter()
router.register(r'summer/', SummerSalesAPIView, basename='summer sales')
router.register(r'fall/', FallSalesAPIView, basename='fall sales')
router.register(r'winter/', WinterSalesAPIView, basename='winter sales')

urlpatterns = [
    path(r'v1/sales_summary/', SalesSummaryAPIView.as_view(), name='Sales Summary'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns.append(path(r'v1/sales/', include(router.urls)))