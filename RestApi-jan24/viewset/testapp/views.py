from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import Employeeserializer
# Create your views here.
class EmployeeCRUDview(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
