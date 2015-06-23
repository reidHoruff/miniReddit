from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'www.views.home'),
    url(r'^register/$', 'www.views.register'),
    url(r'^r/(?P<subreddit>[0-9a-zA-Z_]+)/$', 'www.views.subreddit'),
    url(r'^r/(?P<subreddit>[0-9a-zA-Z_]+)/post/(?P<post_id>[0-9]+)/$', 'www.views.view_post'),
    url(r'^createsub/$', 'www.views.create_sub'),
    url(r'^submit/$', 'www.views.submit'),
    url(r'^login/$', 'www.views._login'),

    #async sniper stuff
    url(r'^async/register/$', 'www.async.register'),
    url(r'^async/comment/$', 'www.async.comment'),
    url(r'^async/createsub/$', 'www.async.create_sub'),
    url(r'^async/submit/$', 'www.async.submit'),
    url(r'^async/logout/$', 'www.async._logout'),
    url(r'^async/login/$', 'www.async._login'),

    url(r'^admin/', include(admin.site.urls)),
)
