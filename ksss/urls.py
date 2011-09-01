from django.conf.urls.defaults import patterns, include, url
from ksss.web import views 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', views.hello),
    (r'^home/$', views.home),
    (r'^langholmen/$', views.langholmen),
    (r'^base/$', views.base),
    (r'^boats/$', views.boats),
    (r'^new_damage/$', views.add_damage),
    (r'^new_damage/thanks/$', views.thanks),
    (r'^damage/edit/(\d+)/$', views.add_damage),
    (r'^new_boat/$', views.add_boat),
    (r'^boats/edit/(\d+)/$', views.edit_boat),
    (r'^boats/delete/(\d+)/$', views.delete_boat),
    # Examples:
    # url(r'^$', 'ksss.views.home', name='home'),
    # url(r'^ksss/', include('ksss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
