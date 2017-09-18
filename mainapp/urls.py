from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'mainapp/home.html')),
    url(r'^auth/$', auth_view, name = 'check'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^projects/$', projects, name = 'projects'),
    url(r'^events/$', events, name = 'events'),
    url(r'^team/$', team, name = 'team'),

]
