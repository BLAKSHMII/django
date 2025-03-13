from django.shortcuts import render
from testapp.models import employee
# Create your views here.
def read(request):
    emp_list = employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})