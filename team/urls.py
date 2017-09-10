from django.conf.urls import url
from team import views

app_name = 'team'

urlpatterns = [
    url(r'^main/$',views.MainPage.as_view(),name='main'),
    url(r'^members/$',views.ListTeam.as_view(),name='all'),
    url(r'^create/$',views.CreateMember.as_view(),name='create'),
    url(r'^edit/(?P<pk>\d+)/$',views.EditMember.as_view(),name='edit'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteMember.as_view(),name='delete'),
]
