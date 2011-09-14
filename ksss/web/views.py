# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ksss.web import models
from ksss.web.forms import AddDamage, AddBoat, EditBoat, News
from django.contrib.auth.decorators import login_required

@login_required
def base(request):
    return render_to_response('base.html') 

@login_required
def langholmen(request):
    return render_to_response('langholmen.html')

@login_required
def home(request):
    return render_to_response('home.html', {
        'latest_news': models.News.objects.order_by('-posted')
    }, context_instance=RequestContext(request))

@login_required
def edit_news(request, news_id=None):
    if request.method == 'POST':
        if news_id:
            to_edit = models.News.objects.get(id=news_id)
            form = News(request.POST, instance = to_edit)
        else: 
            form = News(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')

    elif news_id:
        to_edit = get_object_or_404(models.News, id=news_id)
        form = News(instance = to_edit)
    else:
        form = News()
    return render_to_response('add.html', {
        'form': form
    }, context_instance=RequestContext(request))

@login_required
def one_news(request, news_id):
    newsitem = models.News.objects.get(id=news_id)
    latest_news = models.News.objects.order_by('-posted')[0:4]
    return render_to_response('news.html', {
        'newsitem': newsitem,
        'latest_news': latest_news
    }, context_instance=RequestContext(request))

@login_required
def boat(request, boat_id):
    boat = models.Boat.objects.get(id=boat_id)

    current_damages = False
    repaired_damages = False

    for damage in boat.reporteddamage_set.all():
        if damage.repaired == False:
            current_damages = True
        if damage.repaired == True:
            repaired_damages = True

    return render_to_response('boat.html', {
        'boat': boat,
        'current_damages': current_damages,
        'repaired_damages': repaired_damages
    }, context_instance=RequestContext(request))

@login_required
def boats(request):
    return render_to_response('boats.html', {
        'Boats': models.Boat.objects.all(), 
        })

@login_required
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

@login_required
def edit_boat(request, boat_id):
    to_edit = models.Boat.objects.get(id=boat_id)
    if request.method == 'POST':
        form = EditBoat(request.POST, instance = to_edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_damage/thanks/')
    else:
        try:
            boat_id = int(boat_id)
        except ValueError:
            raise Http404()
        form = EditBoat(instance = to_edit)
        
    return render_to_response('edit.html', {
        'form': form
    }, context_instance=RequestContext(request))

@login_required
def delete(request, id, item):
    to_be_deleted = item.objects.get(id=id)
    to_be_deleted.delete()

    return HttpResponseRedirect('/new_damage/thanks/')

@login_required
def damage(request, dmg_id=None):
    if request.method == 'POST':
        if dmg_id:
            to_edit = models.ReportedDamage.objects.get(id=dmg_id)
            form = AddDamage(request.POST, instance = to_edit)
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
        to_edit = models.ReportedDamage.objects.get(id=dmg_id)
        form = AddDamage(instance = to_edit)

    else:
        form = AddDamage()
    return render_to_response('add.html', {
        'form': form
    }, context_instance=RequestContext(request))

@login_required
def thanks(request):
    return render_to_response('thanks.html')
