from django.conf.urls import url
from django.contrib import admin
from .import views
from .views import *



urlpatterns = [
	url(r'^$', event_list , name='list'),
 	url(r'^create/$', event_create , name='event_create'),
 	url(r'^(?P<slug>[\w-]+)/edit/$', event_update ,name='update'),
 	url(r'^(?P<slug>[\w-]+)/delete/$', event_delete, name='delete'),

]