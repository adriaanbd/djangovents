from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from .forms import EventForm, SignUpForm
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

# TODO: Re-implement using Base views (from django.views import View, TemplateView and RedirectView)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'events/signup.html'


class EventList(ListView):
    model = Event
    template_name = 'events/index.html'

@method_decorator(login_required, name='dispatch')
class NewEvent(CreateView):
    model = Event
    form_class = EventForm
    success_url = 'index'  # if not found, defaults go get_absolute_url
    template_name = 'events/new.html'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.creator = self.request.user
            self.object.save()
            return redirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = "events/show.html"


@method_decorator(login_required, name='dispatch')
class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.creator != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    fields = [
        'name', 'event_date', 'time_start', 
        'time_end', 'venue', 'description']
    template_name = 'events/edit.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.creator != self.request.user:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)