from django.shortcuts import render
import datetime,random
def info(request):
    date=datetime.datetime.now()
    name="django"
    prerequisite="python"
    msg_list=["this golden time for you!..",
             "tomorrow will be best day for in your life!..",
             "tommorrow is perfect date for work!..",
             "you will get job early as possible!.."]
    name_list=['samantha','tammana','sneha','harika']
    h=int(date.strftime('%H'))
    if h<12:
        msg="good morning"
    elif h<16:
        msg="good afternoon"
    elif h<21:
        msg="good evining"
    else:
        msg="good night"
    #my_dict={"date":date,"name":name,"prerequisite":prerequisite}
    names=random.choice(name_list)
    msgs=random.choice(msg_list)
    my_dict={"date":date,"name":name,"prerequisite":prerequisite,"names":names,"msgs":msgs,"msg":msg}
    return render(request,'testapp/wish.html',my_dict)


# Create your views here.
