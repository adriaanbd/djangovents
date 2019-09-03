from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .models import Event
from .forms import EventForm, SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect('/events/index')
    else:
        form = SignUpForm()
    return render(request, 'events/signup.html', {'form': form})


def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def show(request, event_id):
    event = Event.objects.get(id=event_id)
    return HttpResponse(f'<h1>{event.name}</h1>')

@login_required  # also takes optional args to redirect to specific path
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

