from django.conf.urls.defaults import patterns, include, url
from ksss.web import views 
from ksss.web import models
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^home/$', views.home),
    (r'^home/new/$', views.news),
    (r'^home/edit/(\d+)$', views.news),
    (r'^langholmen/$', views.langholmen),
    (r'^base/$', views.base),
    (r'^boats/(\d+)/$', views.boat),
    (r'^boats/$', views.boats),
    (r'^boats/new/$', views.add_boat),
    (r'^boats/edit/(\d+)/$', views.edit_boat),
    (r'^boats/delete/(\d+)/$', views.delete, {'item': models.Boat}),
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
