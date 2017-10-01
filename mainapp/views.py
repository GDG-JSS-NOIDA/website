# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import auth
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from django.shortcuts import render_to_response
from django.template import RequestContext

# from .forms import *
from .models import *

# Create your views here.
def handler404(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response

def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
	else:
		return HttpResponseRedirect('/invalid/')
	return render(request, 'mainapp/dashboard.html')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/dashboard/')


def projects():
	pass


def events():
	pass


def team():
	pass
