from django.contrib import admin
from testapp.models import Books
# Register your models here.
class Booksadmin(admin.ModelAdmin):
    list_display=['title','author','pages','price']
admin.site.register(Books,Booksadmin)