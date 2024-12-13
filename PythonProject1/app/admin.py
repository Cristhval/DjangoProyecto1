from django.contrib import admin
from .models import Padre, Hijo

class HijoInline(admin.TabularInline):  # Presenta los datos en columnas
    model = Hijo
    extra = 1  # Número de formularios vacíos para agregar hijos

class PadreAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')  # Columnas en la lista
    search_fields = ('nombre',)  # Campo de búsqueda
    list_filter = ('nombre',)  # Filtros laterales
    inlines = [HijoInline]  # Relación uno a muchos en el formulario

admin.site.register(Padre, PadreAdmin)


from django.contrib import admin
from .models import Zoologico, Animal

class AnimalInline(admin.TabularInline):  # Relación uno a muchos en un formulario
    model = Animal
    extra = 1  # Número de filas vacías para añadir más hijos

@admin.register(Zoologico)
class ZoologicoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "capacidad")  # Mostrar columnas
    search_fields = ("nombre", "ubicacion")  # Búsqueda
    list_filter = ("ubicacion",)  # Filtros
    inlines = [AnimalInline]  # Registrar animales en un solo formulario

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "edad", "estado_salud", "zoologico")  # Presentar columnas
    search_fields = ("nombre", "especie")  # Búsqueda
    list_filter = ("estado_salud", "especie")  # Filtros
