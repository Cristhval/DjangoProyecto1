# app/views.py

from django.shortcuts import render
from .models import Zoologico

def zoologico_list(request):
    zoologicos = Zoologico.objects.all()  # Obtener todos los zoológicos
    return render(request, 'app/zoologico_list.html', {'zoologicos': zoologicos})  # Renderiza la plantilla
