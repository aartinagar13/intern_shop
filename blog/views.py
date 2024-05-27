from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.
def blogHome(request):
    return render(request, 'blog/index.html')
 
def blogPost(request, slug):
    return HttpResponse("hello")



