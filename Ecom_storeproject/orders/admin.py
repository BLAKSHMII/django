from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
