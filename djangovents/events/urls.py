from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('signup/', views.signup, name='signup'),
    path('<int:event_id>', views.show, name='show'),
    path('edit/<int:event_id>', views.edit, name='edit'),
    path('delete/<int:event_id>', views.delete_event, name='delete')    
]
