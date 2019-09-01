from django.shortcuts import render
from django.http import HttpResponse
from .models import Event


def index():
    events = Event.objects.all()
    events_list = ''
    for event in events:
        events_list += f'<li>{event.name}</li>'
    return HttpResponse(f'<ul>{events_list}</ul>')
