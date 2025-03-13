from django.http import HttpResponse
class middlewareexcution(object):
    def __init__(self,get_respose):
        self.get_respose=get_respose
    def __call__(self,request):
        return HttpResponse('<h1>hello quest  wait 2-minites  for view </h2>')
    

