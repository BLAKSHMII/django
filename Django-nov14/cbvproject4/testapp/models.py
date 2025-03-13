from django.db import models

# Create your models here.
class company(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    ceo=models.CharField(max_length=30)
    