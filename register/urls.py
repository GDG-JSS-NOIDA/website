from django.conf.urls import url
from .import views


app_name = 'register'


urlpatterns = [
    url(r'^(\d+)$',views.register,name='register'),
]
