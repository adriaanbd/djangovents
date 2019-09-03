from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event


class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=30, help_text='Required.')
  last_name = forms.CharField(max_length=30, help_text='Required.')
  email = forms.CharField(max_length=254, help_text='Required.')
  class Meta:
    model = User
    fields = [
      'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
      ]

class EventForm(ModelForm):
    required_css_class = 'required'
    class Meta:
      model = Event
      exclude = ['date_created', 'creator']