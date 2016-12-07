from django.shortcuts import render
from home.models import projects
# Create your views here.
def index(request):
    obj = projects.objects.all()
    ret = {}
    for o in obj:
        ret[o.id] = o
    ret['objects'] = obj
    return render(request, "home/index.html",ret)

def project(request, uid = -1):
    page = projects.objects.get(id = int(uid))
    arr =  str(page.images).split(",")
    for i in range(len(arr)):
        arr[i] = page.filepath + arr[i]
    ret = {
        'title': page.title,
        'subtitle': page.subtitle,
        'videos': page.video, 
        'images': arr,
        'text': page.words,
        'filepath':page.filepath
        
    }
    return render(request,"home/project.html", ret)
    
from django.template import RequestContext
from django.shortcuts import render_to_response

def handler404(request):
    response = render_to_response('home/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('home/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response