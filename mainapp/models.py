# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib import auth
from django.utils import timezone
import datetime
from django.db.models import TimeField
from django.core.urlresolvers import reverse  # to use get_absolute_url
# to implement slug (a dynamic name for posts not just the id)
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


# team models
class Team(models.Model):
    # user_id = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    pic = models.ImageField(upload_to='team/',
                            null=True, blank=True, height_field="height_field",
                            width_field="width_field")
    height_field = models.IntegerField(default=0, blank=True)
    width_field = models.IntegerField(default=0, blank=True)
    year = models.IntegerField(default=0, blank=True)
    github_link = models.URLField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    linkedin = models.URLField(
        max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


# projects models
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(max_length=40, blank=True, null=True)
    github_repo = models.CharField(max_length=100, blank=True, null=True)
    live_link = models.CharField(max_length=200, blank=True, null=True)
    # contributors, image are fetched from new tables

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)
    picture = models.ImageField(upload_to='projects/', blank=True, null=True,height_field="height_field",
                                                width_field="width_field")
    height_field = models.IntegerField(default=290, blank=True)
    width_field = models.IntegerField(default=210, blank=True)
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contributors(models.Model):
    name = models.OneToOneField(Team)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.name.name


# events modals
class Event(models.Model):
    event_name = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    #start_time =  models.TimeField()
    #end_time =  models.TimeField()
    content = models.TextField()
    speaker = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    reg_link = models.URLField(max_length=120)
    created_by = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='events/',
                            null=True, blank=True,
                            height_field="height_field",
                            width_field="width_field")
    height_field = models.IntegerField(default=290)
    width_field = models.IntegerField(default=210)

    def __str__(self):
        return self.event_name

    # it can be used in a href in html
    def get_absolute_url(self):
        return reverse("event:detail", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):  # slug implementation
    slug = slugify(instance.event_name)

    if new_slug is not None:
        slug = new_slug
    qs = Event.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_event_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_event_receiver, sender=Event)


class EventImage(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event)
    picture = models.ImageField(upload_to='events/',
                                null=True, blank=True,
                                height_field="height_field",
                                width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.name
