from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.


class ListTeam(generic.ListView):
    fields = ('name', 'user_id', 'github_link', 'gmail',
              'pic', 'description', 'linkedin', 'status')
    model = Team
    template_name = 'team/members.html'  # template name should be members.html
