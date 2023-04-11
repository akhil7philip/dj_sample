from django.contrib import admin
from .models import SalesTwoModel, SalesOneModel

# Register your models here.

class SalesOneModelAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SalesOneModel._meta.get_fields()]
    
admin.site.register(SalesOneModel, SalesOneModelAdmin)