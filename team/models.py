from django.db import models
from django.conf import settings
from django.contrib import auth


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Team(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    pic = models.ImageField(upload_to=upload_location,
                            null=False, blank=True, height_field="height_field",
                            width_field="width_field")
    github_link = models.URLField(max_length=50)
    email = models.EmailField(max_length=250)
    linkedin = models.CharField(
        max_length=250)
    description = models.URLField(max_length=250)

    def __str__(self):
        return self.name
