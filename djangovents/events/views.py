from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Event
from .forms import EventForm


def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def show(request, event_id):
    event = Event.objects.get(id=event_id)
    return HttpResponse(f'<h1>{event.name}</h1>')

def new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event_params = form.save(commit=False)
            event_params.creator = request.user
            event_params.save()
            return HttpResponseRedirect('/events/index')
        else:
            return HttpResponse('<p>Not valid</p>')
    else:
        form = EventForm()
        if request.method == 'GET':
            return render(request, 'events/new.html', {'form': form})

