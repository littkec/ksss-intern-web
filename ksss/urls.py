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
    (r'^batar/$', views.batar),
    (r'^ny_skada/$', views.add_damage),
    (r'^ny_skada/tack/$', views.thanks),
    (r'^ny_bat/$', views.add_boat),
    (r'^batar/edit/(\d+)/$', views.edit_boat),
    # Examples:
    # url(r'^$', 'ksss.views.home', name='home'),
    # url(r'^ksss/', include('ksss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
