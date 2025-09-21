from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer

class AccountView(RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.account
