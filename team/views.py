from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class MainPage(generic.ListView,LoginRequiredMixin):
    template_name = 'team/main.html'
    fields = ('name', 'github_link', 'email',
              'pic', 'description', 'linkedin', 'status')
    model = models.Team
    context_object_name = 'member_details'

class ListTeam(generic.ListView):
    fields = ('name', 'github_link', 'email',
              'pic', 'description', 'linkedin', 'status')
    model = models.Team
    context_object_name = 'member_details'
    template_name = 'team/members.html'  # template name should be members.html

class CreateMember(generic.CreateView,LoginRequiredMixin):

    model = models.Team
    template_name = 'team/create_member.html'
    success_url = reverse_lazy("team:main")
    form_class = forms.MemberCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class EditMember(LoginRequiredMixin,generic.UpdateView):

    model = models.Team
    template_name = 'team/edit_member.html'
    success_url = reverse_lazy("team:main")
    form_class = forms.MemberEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteMember(generic.DeleteView,LoginRequiredMixin):
    model = models.Team
    success_url = reverse_lazy("team:main")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.userId.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
