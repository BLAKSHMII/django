import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormproject.settings')
import django
django.setup()

from faker import Faker #faker =module ,Faker=class
from testapp.models import employee
from random import*   # rondom=module * =all classes
fakedata = Faker()

def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fname=fakedata.name()
        fsal=randint(10000,30000)
        faddr=fakedata.city()
        emp_record=employee.objects.get_or_create(eno=feno,ename=fname,esal=fsal,eaddr=faddr)
n=int(input("enter number employess"))
print(f"{n} inserted successfully.....")
