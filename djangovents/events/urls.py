from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:event_id>', views.show, name='show')
]
