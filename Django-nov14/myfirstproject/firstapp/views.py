from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s='<h1 color="red">Hello this django first application</h2>'
    return HttpResponse(s)
