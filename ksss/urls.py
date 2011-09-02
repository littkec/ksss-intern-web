from django.conf.urls.defaults import patterns, include, url
from ksss.web import views 
from ksss.web import models

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^home/$', views.home),
    (r'^langholmen/$', views.langholmen),
    (r'^base/$', views.base),
    (r'^boats/$', views.boats),
    (r'^boats/new/$', views.add_boat),
    (r'^boats/edit/(\d+)/$', views.edit_boat),
    (r'^boats/delete/(\d+)/$', views.delete, {'item': models.Boat}),
    (r'^damage/new/$', views.damage),
    (r'^damage/edit/(\d+)/$', views.damage),
    (r'^damage/delete/(\d+)/$', views.delete, {'item': models.ReportedDamage}),
    (r'^new_damage/thanks/$', views.thanks),
    # Examples:
    # url(r'^$', 'ksss.views.home', name='home'),
    # url(r'^ksss/', include('ksss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
