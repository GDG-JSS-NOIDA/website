from django.shortcuts import render
from .models import *
from django.http import *
from django.shortcuts import render, redirect

# Create your views here.


def DisplayProjects(request):
	projects = Project.objects.all()
	return render(request, 'projects/home.html', {'projects': projects})