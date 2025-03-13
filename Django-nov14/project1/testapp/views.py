from django.shortcuts import render
import datetime
def wish(request):
    data=datetime.datetime.now()
    my_dict={'insert':data}
    return render(request,'testapp/wish.html',context=my_dict)

# Create your views here.
