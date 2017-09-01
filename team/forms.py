from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from team.models import Team

class MemberCreateForm(ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'github_link', 'email',
                  'pic', 'description', 'linkedin', 'status')


    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['name'].label = 'Full Name'
    #     self.fields['github_link'].label = "GitHub Link"

class MemberEditForm(ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'github_link', 'email',
                  'pic', 'description', 'linkedin', 'status')
