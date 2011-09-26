from django.conf.urls.defaults import patterns, include, url
from ksss.web import views 
from ksss.web import models
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^home/$', views.home),
    (r'^home/new/$', views.edit_news),
    (r'^home/edit/(\d+)/$', views.edit_news),
    (r'^news/(\d+)/$', views.one_news),
    (r'^(langholmen)/$', views.camp),
    (r'^(lokholmen)/$', views.camps),
    (r'^([a-z]*)/news/(\d+)/$', views.one_campnews),
    (r'^inventory/new/$', views.method_splitter, {'GET': views.get_inventory, 'POST': views.post_inventory}),
    (r'^inventory/edit/(?P<id>\d+)/$', views.method_splitter, {'GET': views.get_inventory, 'POST': views.post_inventory}),
    (r'^([a-z]*)/inventory/(\d+)/$', views.inventory),
    (r'^([a-z]*)/building/$', views.camps, {'building': True}),
    (r'^base/$', views.base),
    (r'^boats/$', views.boats),
    (r'^boats/new/$', views.add_boat),
    (r'^boats/edit/(\d+)/$', views.edit_boat),
    (r'^boats/delete/(\d+)/$', views.delete, {'item': models.Boat}),
    (r'^boats/(\d+)/$', views.boat),
    (r'^([a-z]*)/boats/$', views.campboats),
    (r'^damage/new/$', views.damage),
    (r'^damage/edit/(\d+)/$', views.damage),
    (r'^damage/delete/(\d+)/$', views.delete, {'item': models.ReportedDamage}),
    (r'^new_damage/thanks/$', views.thanks),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    # Examples:
    # url(r'^$', 'ksss.views.home', name='home'),
    # url(r'^ksss/', include('ksss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
