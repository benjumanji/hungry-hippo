from django.conf.urls import patterns, include, url

from hungry_hippo.views import hello, current_time, home
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^hello/$', hello),
                       ('^time/$', current_time),
                       ('^$', home),
                      )
    # Examples:
    # url(r'^$', 'hungry_hippo.views.home', name='home'),
    # url(r'^hungry_hippo/', include('hungry_hippo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
