from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='index'),
    path('events/', views.EventList.as_view(), name='index'),
    path('events/new/', views.NewEvent.as_view(), name='new'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='show'),
    path('events/edit/<int:pk>', views.EventUpdateView.as_view(), name='edit'),
    path('events/delete/<int:pk>', views.EventDeleteView.as_view(), name='delete'),
    path('api/events/', views.EventsApiView.as_view())
]
