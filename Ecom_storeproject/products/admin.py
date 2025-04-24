from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'description','image']
admin.site.register(Product, ProductAdmin)
