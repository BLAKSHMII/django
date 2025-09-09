from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstview(request):
    s="hello this from firstview"
    return HttpResponse(s)
def secondview(request):
    s="hello this from second view"
    return HttpResponse(s)
def thirdview(request):
    s='hello this from third view'
    return HttpResponse(s)