import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datafilter.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
from random import *
fake=Faker()
def populate(n):
    for i in range(n):
        feno=randint(100,999)
        fename=fake.name()
        fesal=randint(10000,99999)
        feaddr=fake.city()
        emp_data=Employee.objects.get_or_create(
        eno=feno,
        ename=fename,
        esal=fesal,
        eaddr=feaddr)
n=int(input("Enter no of employee records .........."))
populate(n)
print(f"{n} Employees records inserted successfully..................")