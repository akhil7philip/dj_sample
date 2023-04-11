from email.policy import default
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import FallSalesModel

class FallSalesModelSerializer(serializers.ModelSerializer):
    
    start_time                  = serializers.DateTimeField(required=True)
    end_time                    = serializers.DateTimeField(required=True)
    
    class Meta:
        model   = FallSalesModel
        fields  = '__all__'