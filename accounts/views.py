from django.shortcuts import render

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

		def register(request):
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
		                albums = Album.objects.filter(user=request.user)
		                return render(request, 'music/index.html', {'albums': albums})
		    context = {
		        "form": form,
		    }
		    return render(request, 'accounts/register.html', context)