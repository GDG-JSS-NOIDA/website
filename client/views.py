from django.shortcuts import render
from projects.models import *
from team.models import *
from events.models import *

# Create your views here.
def index(request):
    return render(request, 'client/index.html')

def events(request):
	event  = Event.objects.all()
	now =datetime.datetime.now()
	ongoing = Event.objects.all().filter(start_date__lte= now , end_date__gte=now)
	upcoming= Event.objects.all().filter(start_date__gte=now)
	past = Event.objects.all().filter(end_date__lte=now)
	full_list = []
	for items in ongoing:
		items.category = "ongoing"
		full_list.append(items)
	for items in upcoming:
		items.category = "upcoming"
		full_list.append(items)
	for items in past:
		items.category = "past"
		full_list.append(items)
	print (full_list)
	context = {
	"queryset1": full_list,
	}
	return render(request, 'client/events.html',context)

def team(request):
	team = Team.objects.all()
	return render(request, 'client/team.html', {'teams': team})

def register(request):
    return render(request, 'client/register.html')

def projects(request):
    project = Project.objects.all()
    return render(request, 'client/projects.html', {'projects': project})
