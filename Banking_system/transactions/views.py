from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from accounts.models import Account
from .serializers import TransactionSerializer

class DepositView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = float(request.data.get("amount", 0))
        account = request.user.account
        account.balance += amount
        account.save()
        txn = Transaction.objects.create(account=account, type="deposit", amount=amount)
        return Response(TransactionSerializer(txn).data)

class WithdrawView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = float(request.data.get("amount", 0))
        account = request.user.account
        if account.balance < amount:
            return Response({"error": "Insufficient balance"}, status=400)
        account.balance -= amount
        account.save()
        txn = Transaction.objects.create(account=account, type="withdraw", amount=amount)
        return Response(TransactionSerializer(txn).data)

class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(account=request.user.account).order_by("-timestamp")
        return Response(TransactionSerializer(transactions, many=True).data)
