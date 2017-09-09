from django.contrib.auth import get_user_model
from django.forms import ModelForm
from register.models import Register

class RegisterForm(ModelForm):

    class Meta:
        model = Register
        fields = ('name', 'adm_no', 'email', 'contact_no')
