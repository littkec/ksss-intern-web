# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from ksss.web import models
from ksss.web.forms import AddDamage, AddBoat, EditBoat, News, Inventory, Upload
from django.contrib.auth.decorators import login_required

@login_required
def base(request):
    return render_to_response('base.html') 

@login_required
def camps(request, camp, current_inventorytype_id=None, building=False):
    if current_inventorytype_id:
        current_inventorytype = models.InventoryType.objects.get(id=current_inventorytype_id)
    else:
        current_inventorytype = None

    if building == True:
        building_objects = models.Buildings.objects.all()
    else: 
        building_objects = None

    return render_to_response('camps.html', {
        'camp': camp,
        'inventory': models.Inventory.objects.all(),
        'inventorytype': models.InventoryType.objects.all(),
        'current_inventorytype': current_inventorytype,
        'building_objects': building_objects
    }, context_instance=RequestContext(request))

@login_required
def camp(request, camp):
    camp = models.Camp.objects.get(slug=camp)
    return render_to_response('campnews.html', {
        'camp': camp,
        'inventorytype': models.InventoryType.objects.all(),
        'news': models.News.objects.all()
    }, context_instance=RequestContext(request))

@login_required
def one_campnews(request, camp, news_id):
    camp = models.Camp.objects.get(slug=camp)
    return render_to_response('one_campnews.html', {
        'camp': camp,
        'inventorytype': models.InventoryType.objects.all(),
        'news': models.News.objects.all(),
        'current_news': models.News.objects.get(id=news_id)
    }, context_instance=RequestContext(request))
    
    
@login_required
def inventory(request, camp, inventory_type_id):
    camp = models.Camp.objects.get(slug=camp)
    if inventory_type_id == str(0):
        inventory_type = 0
    else:
        inventory_type = get_object_or_404(models.InventoryType, id=inventory_type_id)
    

    return render_to_response('inventory.html', {
        'camp': camp,
        'inventorytype': models.InventoryType.objects.all(),
        'news': models.News.objects.all(),
        'inventory': models.Inventory.objects.all(),
        'current_inventorytype': inventory_type
    }, context_instance=RequestContext(request))

@login_required
def campboats(request, camp):
    camp = models.Camp.objects.get(slug=camp)
    
    return render_to_response('campboats.html', {
        'camp': camp,
        'inventorytype': models.InventoryType.objects.all(),
        'news': models.News.objects.all(),
        'Boats': models.Boat.objects.all(),
    }, context_instance=RequestContext(request))
    

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
def method_splitter(request, GET=None, POST=None, id=None):
    if request.method == 'GET' and GET is not None:
        return GET(request, id)
    elif request.method == 'POST' and POST is not None:
        return POST(request, id)
    else:
        raise Http404()
        

@login_required
def get_inventory(request, id):
    if id:
        to_edit = get_object_or_404(models.Inventory, id=id)
        form = Inventory(instance = to_edit)
    else:
        form = Inventory()
    return render_to_response('add.html', {
        'form': form
    }, context_instance=RequestContext(request))

@login_required
def post_inventory(request, id):
    if id:
        to_edit = models.Inventory.objects.get(id=id)
        form = Inventory(request.POST, instance = to_edit)
    else:
        form = Inventory(request.POST)
    if form.is_valid():
        form.save()
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

@login_required
def method_splitter_upload(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    else:
        raise Http404()

@login_required
def get_upload(request):
    form = Upload()
    return render_to_response('upload.html', {
        'form': form
    }, context_instance=RequestContext(request))

@login_required
def post_upload(request):
    form = Upload(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/new_damage/thanks/')
    else:
        form = Upload()
    return render_to_response('upload.html', {
        'form': form
    }, context_instance=RequestContext(request))

@login_required
def view_media(request, position=None):
    
    return render_to_response('media.html', {
        'media': models.Upload.objects.all()
    }, context_instance=RequestContext(request))
    

    
