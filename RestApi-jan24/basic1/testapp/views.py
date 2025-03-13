from django.shortcuts import render
from testapp.serializers import EmployeeSerializer
from rest_framework import viewsets
from testapp.models import Employee
# Create your views here.
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
class EmployeeCRUDview(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[BasicAuthentication]
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    