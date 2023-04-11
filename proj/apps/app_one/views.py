from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import  status, viewsets
from .models import SummerSalesModel, WinterSalesModel, FallSalesModel
from .tasks import fetch_sales_summary_records, fetch_summer_sales_records, fetch_fall_sales_records, fetch_winter_sales_records
from .serializers import FallSalesModelSerializer

# Create your views here.

class SalesSummaryAPIView(APIView):
    def get(self, request):
        data = fetch_sales_summary_records()
        return Response(data)

class FallSalesAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
        
    queryset            = FallSalesModel.objects.all()
    serializer_class    = FallSalesModelSerializer
    
class SummerSalesAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
        
    queryset            = SummerSalesModel.objects.all()

    def create(self, request, pk=None): 
        msg = fetch_sales_summary_records()
        return Response({"message": msg}, status = status.HTTP_200_OK)
        
class WinterSalesAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
        
    queryset            = WinterSalesModel.objects.all()
    