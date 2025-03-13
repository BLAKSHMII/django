from django.shortcuts import render
def info(request):
    s1="python"
    s2="django"
    s3="restAPI"
    subjects={'s1':s1,"s2":s2,"s3":s3}
    return render(request,'testapp/wish.html',subjects)
# Create your views here.
