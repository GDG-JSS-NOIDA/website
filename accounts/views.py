from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login 
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout
#from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.http import HttpResponseRedirect, HttpResponse


class UserFormView(View):
	form_class = UserForm
	template_name = 'accounts/registration_form.html'

	def get(self, request): # get request method #display blank form
		form = self.form_class(None) #its none because user gets empty form
		return render(request, self.template_name, {'form' : form})
	def post(self, request): # post request method #procee form data into database
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns user objects if credentials are correct
			user = authenticate(username=username, password=password) #verifies the entered credentials with that saved in database

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('#') # after log in get them redirected to home page

		return render(request, self.template_name, {'form' : form})	

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context)

def register(request):
    if request.user.is_authenticated():
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    return render(request, 'index.html')
        context = {
            "form": form,
        }
        return render(request, 'accounts/registration_form.html', context)
    else:
        return HttpResponseRedirect('/')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                return render(request, 'accounts/index.html')
            else:
                return render(request, 'accounts/index.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
    return render(request, 'accounts/login.html')



		