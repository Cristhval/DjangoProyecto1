# proyecto_admin/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL del panel de administración
    path('', include('app.urls')),    # Incluye las URLs de la app en la ruta raíz
]
