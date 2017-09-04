from django import forms
from .models import Event,Image

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = [
		"event_name",
		"start_date",
		"end_date",
		"content",
		"speaker",
		"status",
		"reg_link",
		]
	class Meta:
		model  = Image
		fields  = "__all__"

