from django.db import models

# Create your models here.
from django.db import models
from accounts.models import Account

class Transaction(models.Model):
    TYPE_CHOICES = (
        ("deposit", "Deposit"),
        ("withdraw", "Withdraw"),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
