from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=50)
    adm_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    contact_no = models.BigIntegerField()

    def __str__(self):
        return self.name
