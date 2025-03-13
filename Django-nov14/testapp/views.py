from django.shortcuts import render
from django.http import HttpResponse
def first_view(request):
    return HttpResponse("<h1>this is first view</h2>")

# Create your views here.
def second_view(request):
    return HttpResponse("<h1>this is second view</h2>")

# Create your views here.
def third_view(request):
    return HttpResponse("<h1>this is third view</h2>")

# Create your views here.
