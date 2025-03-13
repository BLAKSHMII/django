from django.shortcuts import render
from django.http import HttpResponse
def wish1(request):
    s="<h1>hello this is a first app1</h>"
    return HttpResponse(s)

# Create your views here.
