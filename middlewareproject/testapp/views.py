from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  welcome(request):
    print("this is excuted by view" )
    return HttpResponse('<h1> this custome welcome</h1>')