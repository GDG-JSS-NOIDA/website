from django.conf.urls import url
from . import views


app_name =  "accounts"

urlpatterns = [
# url(r'^register/$' , views.UserFormView.as_view() , name = 'register' ),
url(r'^register/$', views.register, name='register'),
url(r'^logout_user/$', views.logout_user, name='logout_user'),
url(r'^login_user/$', views.login_user, name='login_user'),
]