from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request,'testapp/wish.html')
def movies(request):
    head="Movies Information"
    s1="OG will come......"
    s2="GAME Changer will come....."
    s3="DEVARA will come..."
    type="movies"
    my_dict={"head":head,"s1":s1,"s2":s2,'s3':s3,"type":type}
    return render(request,'testapp/news.html',my_dict)

def sports(request):
    head="Sports Information"
    s1="81st runs...."
    s2="khohli runs 200....."
    s3="nest IPL  march 2025..."
    type="sports"
    my_dict={"head":head,"s1":s1,"s2":s2,'s3':s3,"type":type}
    return render(request,'testapp/news.html',my_dict)
def politics(request):
    head="politics Information"
    s1="cm chandrababu...."
    s2="duputy cm pawan kalyan....."
    s3="next cm?????..."
    type="politics"
    my_dict={"head":head,"s1":s1,"s2":s2,'s3':s3,"type":type}
    return render(request,'testapp/news.html',my_dict)