from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/', views.events, name='events'),
    url(r'^team/', views.team, name='team'),
    url(r'^register/', views.register, name='register'),
    url(r'^projects/', views.projects, name='projects'),
    
]