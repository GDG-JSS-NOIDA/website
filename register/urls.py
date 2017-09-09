from django.conf.urls import url
from .import views


app_name = 'register'


urlpatterns = [
    url(r'^$',views.Registration,name='regist'),
]
