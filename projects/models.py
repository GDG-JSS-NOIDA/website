from django.db import models

# Create your models here.
		

class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=300)
	github_repo = models.CharField(max_length=100)
	live_link = models.CharField(max_length=200)
	#contributors, image are fetched from new tables

	def __str__(self):
		return self.name


class Image(models.Model):
	name = models.CharField(max_length=100)
	project = models.ForeignKey(Project)
	picture = models.ImageField(upload_to = 'projects', blank = True, null = True)
	
	def __str__(self):
		return self.name


class Contributors(models.Model):
	name = models.CharField(max_length=100)
	project = models.ForeignKey(Project)

	def __str__(self):
		return self.name
