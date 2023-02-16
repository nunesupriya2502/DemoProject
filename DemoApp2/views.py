from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f3(request):
    return HttpResponse("<h2>hello user !!! from demoapp2 f3()</h2><hr/>")
def f4(request):
    return HttpResponse("<h3>hello user !! from demoapp2 f4()</h3><hr/>")