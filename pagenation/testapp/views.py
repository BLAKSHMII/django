from django.shortcuts import render
from rest_framework import generics
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from testapp.pagination import mypagination,mypagination2,mypagination3
# from rest_framework.pagination import PageNumberPagination
# # Create your views here.
# class mypagination(PageNumberPagination):
#     page_size=20
#     page_query_param='mypage'
#     page_size_query_param='num'
#     max_page_size=15
class EmployeeListview(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class=mypagination
    pagination_class=mypagination2
    pagination_class=mypagination3
