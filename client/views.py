from django.shortcuts import render
from projects.models import *
from team.models import *

# Create your views here.
def index(request):
    return render(request, 'client/index.html')

def events(request):
    return render(request, 'client/events.html')

def team(request):
    team = Team.objects.all()
    return render(request, 'client/team.html', {'teams': team})

def register(request):
    return render(request, 'client/register.html')

def projects(request):
    project = Project.objects.all()
    return render(request, 'client/projects.html', {'projects': project})
