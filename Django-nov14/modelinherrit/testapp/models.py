from django.db import models

# Create your models here.
# abstract model inheritance
class contactinfo(models.Model):
    Name=models.CharField(max_length=30)
    email=models.EmailField()
    addr=models.CharField(max_length=30)
class student(contactinfo):
    rno=models.IntegerField()
    marks=models.IntegerField()
class teacher(contactinfo):
    subject=models.CharField(max_length=30)
    sal=models.FloatField()

