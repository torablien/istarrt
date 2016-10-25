from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html")
    
def project(request, uid=-1):
    uid = uid
    ret = {'uid':uid}
    return render(request,"home/project.html", ret)