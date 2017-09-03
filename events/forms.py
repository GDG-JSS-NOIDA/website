from django import forms
from .models import Event


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
            "image",
        ]
