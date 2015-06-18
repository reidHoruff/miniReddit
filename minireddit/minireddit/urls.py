from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'www.views.home'),
    url(r'^register/$', 'www.views.register'),
    url(r'^submit/$', 'www.views.submit'),
    url(r'^login/$', 'www.views._login'),

    #async sniper stuff
    url(r'^async/register/$', 'www.async.register'),
    url(r'^async/submit/$', 'www.async.submit'),
    url(r'^async/logout/$', 'www.async._logout'),
    url(r'^async/login/$', 'www.async._login'),

    url(r'^admin/', include(admin.site.urls)),
)
