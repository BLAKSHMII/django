from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    balance = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.balance}"
