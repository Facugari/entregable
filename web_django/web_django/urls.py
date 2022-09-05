
from django.contrib import admin
from django.urls import path
from servicio_turistico.views import home, cargar_wedding, cargar_corpo, cargar_turismo
from servicio_turistico.views import busqueda_wedding, buscar, busqueda_corpo, buscar_corpo, buscar_turismo,busqueda_turismo



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('cargar_wedding/', cargar_wedding),
    path('cargar_corpo/', cargar_corpo),
    path('cargar_turismo/', cargar_turismo),
    path('busqueda_wedding/', busqueda_wedding),
    path('buscar/', buscar),
    path('busqueda_corpo/', busqueda_corpo),
    path('buscar_corpo/', buscar_corpo),
    path('busqueda_turismo/', busqueda_turismo),
    path('buscar_turismo/', buscar_turismo),
]

