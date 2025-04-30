import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormproject.settings')
django.setup()
from testapp.models import Employee
from random import *
from faker import Faker
fake=Faker()
def populate(n):
    for i in range(n):
        feno=randint(100,999)
        fename=fake.name()
        fesal=randint(10000,99999)
        feaddr=fake.address()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
n=int(input("enter no of records!....."))
populate(n)
print(f"{n} is inserted successfully!...")

