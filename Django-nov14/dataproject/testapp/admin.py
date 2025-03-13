from django.contrib import admin
from testapp.models import emp
# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display= ['id','eno','ename','esal','eaddr' ]
admin.site.register(emp,empadmin)
