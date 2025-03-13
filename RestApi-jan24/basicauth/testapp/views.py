from django.shortcuts import render
from rest_framework import viewsets
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class EmployeeCRUDview(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[BaseAuthentication]
    permission_classes=[IsAuthenticated]
