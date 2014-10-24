from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'talsub.views.home', name='home'),
    url(r'^episode_list/$', 'talsub.views.episode_list', name='episode_list'),

    #url(r'^admin/', include(admin.site.urls)),
)
