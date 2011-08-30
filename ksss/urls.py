from django.conf.urls.defaults import patterns, include, url
from ksss.web import views 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', views.hello),
    ('^home/$', views.home),
    ('^langholmen/$', views.langholmen),
    ('^base/$', views.base),
    ('^batar/$', views.batar),
    ('^ny_skada/$', views.add_damage),
    ('^ny_skada/tack/$', views.thanks),
    ('^ny_bat/$', views.add_boat),
    # Examples:
    # url(r'^$', 'ksss.views.home', name='home'),
    # url(r'^ksss/', include('ksss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
