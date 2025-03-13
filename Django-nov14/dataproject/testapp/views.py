from django.shortcuts import render
from testapp.models import emp
# Create your views here.
def empdata(request):
    emp_list =emp.objects.all()#select *from employyee
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',my_dict)