from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    required_css_class = 'required'
    class Meta:
      model = Event
      exclude = ['date_created']