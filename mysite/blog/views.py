from django.shortcuts import render
from blog.models import BlogPost
from django.template import RequestContext
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'index.html')


def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')
    return render(request,'archive.html',{'posts' : posts})


def create(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body =request.POST.get('body'),
        ).save()
    return HttpResponseRedirect('/blog')