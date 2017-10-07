from django.db import models
from mainapp.models import Event
# Create your models here.

class Register(models.Model):
    eventid = models.ForeignKey(Event)
    name = models.CharField(max_length=50)
    adm_no = models.CharField(max_length=10)
    branch = models.CharField(max_length=30)
    year = models.IntegerField()
    email = models.EmailField(max_length=50)
    contact_no = models.BigIntegerField()

    def __str__(self):
        return self.name
