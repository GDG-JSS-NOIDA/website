from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'client/index.html')

def events(request):
    return render(request, 'client/events.html')

def team(request):
    return render(request, 'client/team.html')

def register(request):
    return render(request, 'client/register.html')
