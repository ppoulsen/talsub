#
# urls.py
# This module connects URLs to controllers (named views in Django)
#

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'talsub.views.home', name='home'),
                       url(r'^episode_list/$', 'talsub.views.episode_list', name='episode_list'),
                       url(r'^transcript/$', 'talsub.views.transcript', name='transcript'),

                       # url(r'^admin/', include(admin.site.urls)),
)
