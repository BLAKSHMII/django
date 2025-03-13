from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import Nameserializer
from rest_framework.viewsets import ViewSet
# Create your views here.
class Testveiwset(ViewSet):
    def list(self,request,*args,**kwargs):
        color=["red","green","yellow","blue","pink"]
        return Response({"msg":"This response is from list method",'color':color})
    def retrieve(self,request,pk=None):
        color=["red","green","yellow","blue","pink"]
        return Response({"msg":"This response is from Retrieve method",'color':color})
    def update(self,request,pk=None):
        color=["red","green","yellow","blue","pink"]
        return Response({"msg":"This response is from Update method",'color':color})
    def partial_update(self,request,pk=None):
        color=["red","green","yellow","blue","pink"]
        return Response({"msg":"This response is from Partial method",'color':color})
    def destroy(self,request,pk=None):
        color=["red","green","yellow","blue","pink"]
        return Response({"msg":"This response is from Destroy method",'color':color})
class Testapiveiw(APIView):
    def put(self,request,*args,**kwargs):
        return Response({"msg:This response is from PUT method"})
    def delete(self,request,*args,**kwargs):
        return Response({"msg:This response is from DELETE method"})
    def patch(self,request,*args,**kwargs):
        return Response({"msg:This response is from PATCH method"})
    def post(self,request,*args,**kwargs):
        serializer=Nameserializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} ,Happy ending of rest_frame work class'.format(name)
            return Response({"msg":msg})
        else:
            return Response(serializer.error,status=400)
    def get(self,request,*args,**kwargs):
        color=["red","green","yellow","blue"]
        return Response({"msg":"HAPPY WOMENS DAY","colors":color})
        # here Response is rest_frame work class it convert the python object into json_data