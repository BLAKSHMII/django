from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Max,Min,Sum,Count
from django.db.models.functions import Lower
# Create your views here.
def empdata_view(request):
    #emp_list=Employee.objects.all()
    #print(type(emp_list)) #emp_list==queryset type
    #emp_list=Employee.objects.filter(esal__gte=12000)
    #emp_list=Employee.objects.filter(esal__lte=12000)
    #emp_list=Employee.objects.filter(ename__contains='sunny')
    #emp_list=Employee.objects.filter(ename__startswith='s')
    #emp_list=Employee.objects.exclude(ename__startswith='s')
    #emp_list=Employee.objects.filter(~Q(ename__startswith='s')) #without s
    #emp_list=Employee.objects.filter(ename__endswith='s')
    #emp_list=Employee.objects.filter(id__in=[1,3,5])
    #emp_list=Employee.objects.filter(ename__startswith='s')|Employee.objects.filter(esal__lte=12000)
    #emp_list=Employee.objects.filter(ename__startswith='s') & Employee.objects.filter(esal__lte=12000)
    #emp_list=Employee.objects.filter(ename__startswith='s',esal=12000)
    emp_list=Employee.objects.all().order_by('eno')
    emp_list=Employee.objects.all().order_by('-eno')
    emp_list=Employee.objects.all().order_by('ename')
    emp_list=Employee.objects.all().order_by(Lower("ename"))

    return render(request,'testapp/index.html',{'emp_list':emp_list})
def aggregate_view(request):
    avg=Employee.objects.all().aggregate(Avg('esal'))
    max=Employee.objects.all().aggregate(Max('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'],'max':max['esal__max'],
	'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)