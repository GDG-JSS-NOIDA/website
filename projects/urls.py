from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.DisplayProjects, name='display_projects'),
    url(r'^list/$', views.ProjectDashboard, name='project_dashboard'),
    url(r'^edit/(\d+)/$', views.EditProject, name='edit_project'),
    url(r'^view/(\d+)/$', views.ViewProject, name='view_project'),
    url(r'^remove/(\d+)/$', views.RemoveProject, name='remove_project'),
    url(r'^view/(\d+)/addImage$', views.AddImage, name='add_image'),
]

