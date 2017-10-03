from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from register.models import Register


class RegisterForm(ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    adm_no = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Admission Number'}))
    branch = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Branch'}))
    year = forms.IntegerField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Year'}))
    email = forms.EmailField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    contact_no = forms.IntegerField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
    class Meta:
        model = Register
        fields = '__all__'
        exclude = ['eventid']
