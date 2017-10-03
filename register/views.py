from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.core.urlresolvers import reverse_lazy
# Create your views here.


def register(request, event_id):
    form = RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.event_id = event_id
            f.save()
            return HttpResponseRedirect('/events/?r=true')
    else:
        form = RegisterForm()
        return render(request, 'client/register.html', {'form': form})
