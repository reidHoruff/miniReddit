from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'www.views.home'),
    url(r'^register/$', 'www.views.register'),

    #async sniper stuff
    url(r'^async/register/$', 'www.async.register'),

    url(r'^admin/', include(admin.site.urls)),
)
