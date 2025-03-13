from django.shortcuts import render
import datetime
def wish(request):
    data=datetime.datetime.now()
    name="siri"
    rollno=12
    marks=90
    msg="hell guest"
    h=int(data.strftime('%H'))
    if h<12:
        msg+="good morning"
    elif h<16:
        msg+="good after noon"
    elif h<21:
        msg+="good evening"
    else:
        msg+="good night"
    my_dict={'insert':data,'name':name,'rollno':rollno,'marks':marks,'msgs':msg}
    return render(request,'testapp/wish.html', context= my_dict)
# Create your views here.
