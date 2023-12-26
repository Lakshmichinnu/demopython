from django.urls import path
from . import views


urlpatterns = [
    path('', views.add, name=''),
    path('delete/<int:taskid>/',views.delete,name='delete'),
]