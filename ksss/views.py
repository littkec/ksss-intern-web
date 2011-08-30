from django.http import HttpResponse
from django.shortcuts import render_to_response

def base(request):
    return render_to_response('base.html') 

def hello(request):
    return HttpResponse("Hello World!")

def css(requeset):
    return HttpResponse('css/nav.css')
