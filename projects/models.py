from django.db import models
from team.models import Team

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(max_length=40, blank=True, null=True)
    github_repo = models.CharField(max_length=100, blank=True, null=True)
    live_link = models.CharField(max_length=200, blank=True, null=True)
    # contributors, image are fetched from new tables

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)
    picture = models.ImageField(upload_to='media/projects/', blank=True, null=True)

    def __str__(self):
        return self.name


# to be linked from user table, all the members
class Contributors(models.Model):
    name = models.OneToOneField(Team)
    project = models.ManyToManyField(Project)
    

    def __str__(self):
        return self.name.name
