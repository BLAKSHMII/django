from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'type', 'amount', 'timestamp']  # show key info

admin.site.register(Transaction, TransactionAdmin)
