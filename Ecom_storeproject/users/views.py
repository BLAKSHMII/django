from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer


# Register View: Handles user registration
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", "")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)

        if email and User.objects.filter(email=email).exists():
            return Response({"error": "Email already in use"}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)

        return Response({
            "message": "User registered successfully",
            "user": UserSerializer(user).data  # Return serialized user data
        })


# Login View: Handles user login
class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({
                "message": "Login successful",
                "user": UserSerializer(user).data  # Return serialized user data
            })
        return Response({"error": "Invalid credentials"}, status=400)


# Profile View: Displays the authenticated user's profile
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    def get(self, request):
        user = request.user  # Get the currently authenticated user
        return Response({
            "user": UserSerializer(user).data  # Return serialized user data
        })


# Logout View: Logs out the user
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    def post(self, request):
        logout(request)  # Log out the user (clear session)
        return Response({"message": "Logout successful"}, status=200)
