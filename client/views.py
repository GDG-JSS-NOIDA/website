from django.shortcuts import render
# from projects.models import *
# from team.models import *
# from events.models import *
from mainapp.models import *
from django.utils import timezone
# Create your views here.


def index(request):
    return render(request, 'client/index.html')


def events(request):
    event = Event.objects.all()
    now = timezone.now()
    ongoing = Event.objects.filter(start_date__lte=now, end_date__gte=now)
    upcoming = Event.objects.filter(start_date__gte=now)
    past = Event.objects.filter(end_date__lte=now)
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

    context = {
        "queryset1": full_list,
    }
    print(context)
    return render(request, 'client/events.html', context)


def team(request):
    team1 = Team.objects.filter(status=True).order_by('-year')
    team2 = Team.objects.filter(status=False).order_by('-year')
    return render(request, 'client/team.html', {'teams1': team1, 'teams2': team2})


def register(request):
    return render(request, 'client/register.html')


def projects(request):
    project = Project.objects.all()
    return render(request, 'client/projects.html', {'projects': project})
