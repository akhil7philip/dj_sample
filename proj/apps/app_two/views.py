from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import fetch_product_list

# Create your views here.

class ProductAPIView(APIView):
    def get(self, request):
        data = fetch_product_list()
        return Response(data)