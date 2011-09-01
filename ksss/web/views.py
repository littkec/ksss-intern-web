# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ksss.web import models
from ksss.web.forms import AddDamage, AddBoat, EditBoat

def base(request):
    return render_to_response('base.html') 

def hello(request):
    return HttpResponse("Hello World!")

def langholmen(request):
    return render_to_response('langholmen.html')

def home(request):
    return render_to_response('home.html')

def boats(request):
    return render_to_response('boats.html', {
        'Boats': models.Boat.objects.all(), 
        })

def add_boat(request):
    if request.method == 'POST':
        form = AddBoat(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_damage/thanks/')
    else:
        form = AddBoat()
    return render_to_response('add.html', {
        'form': form
    }, context_instance=RequestContext(request))

def edit_boat(request, boat_id):
    if request.method == 'POST':
        edit_id = models.Boat.objects.get(id=boat_id)
        form = EditBoat(request.POST, instance = edit_id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_damage/thanks/')
    else:
        try:
            boat_id = int(boat_id)
        except ValueError:
            raise Http404()
        form = EditBoat(
            initial = {
            'boat_type': models.Boat.objects.get(id=boat_id).boat_type,
            'name': models.Boat.objects.get(id=boat_id).name,
            'motor': models.Boat.objects.get(id=boat_id).motor,
            'motor_hp': models.Boat.objects.get(id=boat_id).motor_hp,
            'bought': models.Boat.objects.get(id=boat_id).bought,
            'service': models.Boat.objects.get(id=boat_id).service,
            'location': models.Boat.objects.get(id=boat_id).location
        })
        
    return render_to_response('edit.html', {
        'Id': models.Boat.objects.get(id=boat_id),
        'form': form
    }, context_instance=RequestContext(request))

def delete(request, id, item):
    to_be_deleted = item.objects.get(id=id)
    to_be_deleted.delete()

    return HttpResponseRedirect('/new_damage/thanks/')

def damage(request, dmg_id=None):
    if request.method == 'POST':
        if dmg_id:
            edit_dmg_id = models.ReportedDamage.objects.get(id=dmg_id)
            form = AddDamage(request.POST, instance = edit_dmg_id)
        else:
            form = AddDamage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_damage/thanks/')
    elif dmg_id:
        try:
            dmg_id = int(dmg_id)
        except ValueError:
            raise Http404()

        form = AddDamage(
        initial = {
            'boat': models.ReportedDamage.objects.get(id=dmg_id).boat,
            'damage': models.ReportedDamage.objects.get(id=dmg_id).damage,
            'description': models.ReportedDamage.objects.get(id=dmg_id).description,
            'actions_taken': models.ReportedDamage.objects.get(id=dmg_id).actions_taken,
            'actions_needed': models.ReportedDamage.objects.get(id=dmg_id).actions_needed
        })
    else:
        form = AddDamage()
    return render_to_response('add.html', {
        'form': form
    }, context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html')
