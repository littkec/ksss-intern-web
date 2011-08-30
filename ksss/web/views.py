# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ksss.web import models
from ksss.web.forms import AddDamage, AddBoat

def base(request):
    return render_to_response('base.html') 

def hello(request):
    return HttpResponse("Hello World!")

def langholmen(request):
    return render_to_response('langholmen.html')

def home(request):
    return render_to_response('home.html')

def batar(request):
    boat_type_list = ['Optimist', 'Motorbåt', 'If', 'Två-Krona'] 
    return render_to_response('boats.html', {'Boats': models.Boat.objects.all(), 'boat_type_list': boat_type_list})

def add_boat(request):
    if request.method == 'POST':
        form = AddBoat(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ny_skada/tack/')
    else:
        form = AddBoat()
    return render_to_response('add.html', {
        'form': form
    }, context_instance=RequestContext(request))

def add_damage(request):
    if request.method == 'POST':
        form = AddDamage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ny_skada/tack/')
    else:
        form = AddDamage()
    return render_to_response('add.html', {
        'form': form
    }, context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html')
