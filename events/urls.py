from django.conf.urls import url
from django.contrib import admin
from .import views



urlpatterns = [
	url(r'^$', views.event_list , name='list'),
 	url(r'^create/$', views.event_create , name='event_create'),
 	url(r'^(?P<slug>[\w-]+)/edit/$', views.event_update ,name='update'),
 	url(r'^(?P<slug>[\w-]+)/delete/$', views.event_delete, name='delete'),

]