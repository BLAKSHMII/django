from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.generic import View
from testapp.mixins import HttpResponseMixin
# Create your views here.

#class based view to dsend jsonresponse  every class based view contain View package
class jsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({"msg":"this msg from GET method"})
        return self.render_to_response(json_data)
    def post(self,request,*args,**kwargs):
        json_data=json.dumps({"msg":"this msg from POST method"})
        return self.render_to_response(json_data)
        # return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=json.dumps({"msg":"this msg from PUT method"})
        return self.render_to_response(json_data)
        # return HttpResponse(json_data,content_type='application/json')
    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({"msg":"this msg from DELETE method"})
        return self.render_to_response(json_data)
        # return HttpResponse(json_data,content_type='application/json')

#         emp_data={
#        'eno':105,
#        'ename':"sunny5",
#        'esal':120000,
#        'eaddr':'hyd'
#         }
#         return JsonResponse(emp_data)


# def empdetails(request):
#     emp_data={
#        'eno':101,
#        'ename':"sunny",
#        'esal':120000,
#        'eaddr':'hyd'
#     }
#     resp='<h1>Employee Number{} Employee Name{} Employee Salary{} Employee Address{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
#     return HttpResponse(resp)

#     #send httpresponse with json

#     json_data=json.dumps(emp_data)
#     return HttpResponse(json_data)

#     # directly send the jsonresponse

# def json(request):
#         data= {
#        'eno':102,
#        'ename':"sunnys",
#        'esal':120000,
#        'eaddr':'vid'
#         }
#         return JsonResponse(data)
