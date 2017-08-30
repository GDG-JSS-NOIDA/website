from django.db import models

class events(models.Models):
	event_name = models.CharField(max_length=250, primary_key=True)
	date = models.CharField(max_length = 100)
	time = models.CharField(max_length = 100)
	speaker = models.CharField(max_length = 100)
	desc = models.CharField(max_length = 1000)
	

