from django.shortcuts import render
from testapp.models import Employee
from  django.db.models import Q
from django.db.models import Avg,Min,Max,Sum,Count
from django.db.models.functions import Lower
# Create your views here.
#values_list===quryset return tuple type
#values()====queryset return dict type------->recommanded method
#only()====>query set return Employee object() 
def aggregate_view(request):
    print(request.user) #print the user name who send request
    avg=Employee.objects.all().aggregate(Avg('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    max=Employee.objects.all().aggregate(Max('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))
    my_dict={'avg':avg['esal__avg'],'min':min['esal__min'],'max':max['esal__max'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)
def ret_view(request):
    emp_list=Employee.objects.all().only('ename','esal')
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/specificcols.html',my_dict)
def retrieve_view(request):
    emp_list=Employee.objects.all()
    # emp_list=Employee.objects.filter(esal__gt=15000)
    # emp_list=Employee.objects.filter(esal__gte=15000)
    # emp_list=Employee.objects.filter(esal__lt=30000)
    # emp_list=Employee.objects.filter(esal__lte=30000)
    # emp_list=Employee.objects.filter(ename__contains='john')
    # emp_list=Employee.objects.filter(eno__in=[1,4,8])
    # emp_list=Employee.objects.filter(id__in=[1,4,8])
    # emp_list=Employee.objects.filter(ename__startswith='s')
    # emp_list=Employee.objects.filter(ename__endswith='s')
    # emp_list=Employee.objects.filter(esal__range=[15000,30000]) #both include --->[ means--inclue
    # emp_list=Employee.objects.filter(esal__range=(15000,30000)) #both include --->( means exclude
    # emp_list=Employee.objects.filter(ename__startswith='s')|Employee.objects.filter(esal__lt=30000)
    #    #OR
    # emp_list=Employee.objects.filter(Q(ename__startswith='a')|Q(esal__lt=30000))
    # emp_list=Employee.objects.order_by('eno') #ascending order
    # emp_list=Employee.objects.order_by('-eno')#decending order
    # emp_list=Employee.objects.order_by('ename')
    # emp_list=Employee.objects.order_by(Lower('ename'))
    q1=Employee.objects.filter(esal__lt=30000)
    q2=Employee.objects.filter(ename__startswith='s')
    q3=q1.union(q2) #union operations
    emp_list=q3
    print(type(emp_list))
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',my_dict)

