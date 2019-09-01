from django.shortcuts import render
from django.http import HttpResponse
from .models import Event


def index(request):
    events = Event.objects.all()
    events_list = ''
    for event in events:
        events_list += f'<li>{event.name}</li>'
    return HttpResponse(f'<h1>Events</h1><ul>{events_list}</ul>')

def show(request, event_id):
    event = Event.objects.get(id=event_id)
    return HttpResponse(f'<h1>{event.name}</h1>')
