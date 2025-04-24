from django.shortcuts import render

from rest_framework import generics, permissions
from .models import CartItem
from .serializers import CartItemSerializer, AddCartItemSerializer

class CartListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return AddCartItemSerializer if self.request.method == 'POST' else CartItemSerializer

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(
            user=self.request.user, product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return cart_item

class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddCartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
