from django.contrib import admin
from testapp.models import employee
# Register your models here.3
class employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
admin.site.register(employee,employeeadmin)
