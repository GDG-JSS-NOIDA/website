from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.core.urlresolvers import reverse_lazy
from mainapp.models import Event
from django.http import *
# Create your views here.


def register(request, event_id):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.eventid = Event.objects.get(id = event_id)
            f.save()
            return HttpResponseRedirect('/events/')
    else:
        form = RegisterForm()
        return render(request, 'client/register.html', {'form': form})
