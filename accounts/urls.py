from django.conf.urls import url, include
from . import views

app_name = "accounts"

urlpatterns = [
url(r'^register/$', views.register, name='register'),
url(r'^logout/$', views.logout_user, name='logout_user'),
url(r'^login/$', views.login_user, name='login_user'),
url(r'^projects/', include('projects.urls', namespace='projects', app_name='projects')),
]

