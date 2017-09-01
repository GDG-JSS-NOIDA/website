from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):  # blueprint of user form
    # password is not in admin user by default hence we have to declare
    # it..widget=forms.PasswordInput = this to to make *** when inputting
    # password
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:  # information about class
        model = User  # user model from admin
        fields = ['username', 'email', 'password']
