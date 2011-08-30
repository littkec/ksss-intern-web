# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from ksss.web import models

def base(request):
    return render_to_response('base.html') 

def hello(request):
    return HttpResponse("Hello World!")

def langholmen(request):
    return render_to_response('langholmen.html')

def home(request):
    return render_to_response('home.html')

def batar(request):
    return render_to_response('boats.html', {'If': models.If.objects.all()})

def add_damage(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('boat', ''):
            errors.append('Ange båtnamn')
        if not request.POST.get('damage', ''):
            errors.append('Ange skada')
        if not errors:

            return HttpResponseRedirect('/batar/ny_skada')
    return render_to_response('add_damage.html', {'errors': errors})
