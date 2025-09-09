from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def display(request):
    date=datetime.datetime.now()
    s="<h1>Hello this Lakshmi Django class</h1>"+str(date)
    msg=s+str(date)
    return HttpResponse(s)
def hyd_jobs(request):
    date=datetime.datetime.now()
    s='<h1> Welcome to Hyd_jobs !..............</h1>'+str(date)
    return HttpResponse(s)
def del_jobs(request):
    date=datetime.datetime.now()
    s='<h1> Welcome to Delhi_jobs !..............</h1>'+str(date)
    return HttpResponse(s)
def vij_jobs(request):
    date=datetime.datetime.now()
    s='<h1> Welcome to Vijavawada_jobs !..............</h1>'+str(date)
    return HttpResponse(s)
def gun_jobs(request):
    date=datetime.datetime.now()
    s='<h1> Welcome to Guntur_jobs !..............</h1>'+str(date)
    return HttpResponse(s)
