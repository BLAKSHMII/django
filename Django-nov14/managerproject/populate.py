import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'managerproject.settings')
import django
django.setup()

from faker import Faker
from testapp.models import employee
from random import *
faker=Faker()

def populate(n):
    for i in range(n):
        feno= randint(1001,9999)
        fename=faker.name()
        fsal=randint(10000,20000)
        feaddr=faker.city()
        emp_record=employee.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fsal,
            eaddr=feaddr)

n=int(input("enter no of employees.."))   
populate(n)
print(f'{n} inserted successfully.......')   
