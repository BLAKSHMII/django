from django.contrib import admin

# Register your models here.
# cart/admin.py
from django.contrib import admin
from .models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'total_price']

    def total_price(self, obj):
        return obj.product.price * obj.quantity
    total_price.short_description = 'Total Price'  # This sets the column name

admin.site.register(CartItem, CartItemAdmin)
