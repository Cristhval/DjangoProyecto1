# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('zoologico/', views.zoologico_list, name='zoologico_list'),  # Ruta para la lista de zoológicos
]
