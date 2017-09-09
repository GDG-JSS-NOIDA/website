from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def Registration(request):
    form = form.RegisterForm()
    if method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            print("Successfully Registerd with the event!")
            return HttpResponseRedirect('/events/?r=true')
    else:
        form = form.RegisterForm()
        return render(request, 'register/event_registeration.html', {'form': form})
