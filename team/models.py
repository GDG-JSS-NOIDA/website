from django.db import models
from django.conf import settings
from django.contrib import auth
from accounts import models


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Team(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    pic = models.ImageField(upload_to=upload_location,
                            null=False, blank=True, height_field="height_field"
                            width_field="width_field")
    github_link = models.CharField(max_length=50)
    gmail = models.EmailField(max_length=250, description=_("Email Address"))
    linkedin = models.CharField(
        max_length=250, description=_("LinkedIn Account"))
    description = models.CharField(max_length=250)
