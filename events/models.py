from __future__ import unicode_literals
from django.db import models
import datetime
from django.db.models import TimeField
from django.core.urlresolvers import reverse  # to use get_absolute_url
# to implement slug (a dynamic name for posts not just the id)
from django.db.models.signals import pre_save

from django.utils.text import slugify


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Event(models.Model):
	event_name = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now =False, auto_now_add = True)
	start_date = models.DateTimeField(default=datetime.date.today)
	end_date = models.DateTimeField(default=datetime.date.today)
	#start_time =  models.TimeField()
	#end_time =  models.TimeField()
	content = models.TextField()
	speaker = models.CharField(max_length = 255)
	status =  models.CharField(max_length = 255)
	reg_link = models.URLField(max_length = 120)
	created_by = models.CharField(max_length= 255)
	slug = models.SlugField(unique=True)
	
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


class Image(models.Model):
	name = models.CharField(max_length= 100)
	event = models.ForeignKey(Event)
	picture = models.ImageField(upload_to='media/events/',
		null = True,blank = True,
		height_field="height_field",
		width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	def __str__(self):
		return self.name
		




