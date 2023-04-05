from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import fetch_sales_summary_records, fetch_summer_sales_records, fetch_fall_sales_records, fetch_winter_sales_records

# Create your views here.

class SalesSummaryAPIView(APIView):
    def get(self, request):
        data = fetch_sales_summary_records()
        return Response(data)

class SummerSalesAPIView(APIView):
    def get(self, request):
        data = fetch_summer_sales_records()
        return Response(data)
    
class FallSalesAPIView(APIView):
    def get(self, request):
        data = fetch_fall_sales_records()
        return Response(data)
    
class WinterSalesAPIView(APIView):
    def get(self, request):
        data = fetch_winter_sales_records()
        return Response(data)