from django.contrib import admin
from .models import ProductOneModel

# Register your models here.

class ProductOneModelAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductOneModel._meta.get_fields()]
    
admin.site.register(ProductOneModel, ProductOneModelAdmin)