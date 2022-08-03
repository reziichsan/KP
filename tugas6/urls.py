from django.urls import path

from . import views

app_name = 'tugas6'

urlpatterns = [
    path('', views.index, name='index'),
]