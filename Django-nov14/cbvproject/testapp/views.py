from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
class HelloWorld(View):
    def get(self,request):
        return HttpResponse('<h1>This is class based view')
class Templatecbv(TemplateView):
    template_name='testapp/result.html'

# Create your views here.
class Templatecbv2(TemplateView):
    template_name='testapp/result2.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs) # it call parent =templatecbv
        context['name']="sunny"
        context['marks']=98
        context['subject']='python'
        return context