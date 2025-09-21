from django.contrib import admin
from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance'] # show username and balance in list view

admin.site.register(Account, AccountAdmin)
