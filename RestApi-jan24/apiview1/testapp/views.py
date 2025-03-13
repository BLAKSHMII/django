from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import Employeeserializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# Create your views here.
class EmployeeListApiview(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
class EmployeeCreateApiview(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
class EmployeeRetrieveApiview(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
class EmployeeUpdateApiview(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
class EmployeeDeleteApiview(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
class EmployeeListCreateApiview(ListAPIView,CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
class EmployeeRetrieveUpdateDeleteApiview(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
# class Employeeview(APIView):
#     def get(self,request,*args,**kwargs):
#         qs=Employee.objects.all()
#         serializer=Employeeserializer(qs,many=True)
#         return Response(serializer.data)