from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.shortcuts import render, redirect

# Create your views here.


def DisplayProjects(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})


def ProjectDashboard(request):
    projects = Project.objects.all()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            c_proj = form.save()
            # return HttpResponseRedirect('/projects/dashboard/')
            # id = Project.objects.get
            return HttpResponseRedirect(
                '/projects/dashboard/view/' + str(c_proj.id))
    else:
        form = ProjectForm()
        return render(request, 'projects/dashboard.html',
                      {'projects': projects, 'form': form})


def EditProject(request, id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/dashboard/')
    else:
        form = ProjectForm(instance=project)
        return render(request, 'projects/edit_project.html',
                      {'project': project, 'form': form})


def ViewProject(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projects/view_project.html', {'project': project})


def RemoveProject(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return HttpResponseRedirect('/projects/dashboard/')


def AddImage(request, id):
	if request.method=="POST":
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			f = form.save(commit = False)
			f.project = Project.objects.get(id=id)
			f.save()
			return HttpResponseRedirect('/projects/dashboard/view/' + str(id))
	else:
		form = ImageForm()
		return render(request, 'projects/add_image.html', {'form': form})