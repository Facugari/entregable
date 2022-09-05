from django.shortcuts import render

from .models import Turismo, Weddings, Corporativos
from .forms import Tourism, Wedding, Corpo
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', context={})

def cargar_wedding(request):
    if request.method ==  'POST':
        mi_formulario = Wedding(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            nuevo_casamiento = Weddings(name=informacion['name'], fecha=informacion['fecha'], precio=informacion['precio'])
            nuevo_casamiento.save()
        return render(request, 'home.html')
    else:
        mi_formulario = Wedding()
    return render(request, 'cargar_wedding.html', {"mi_formulario":mi_formulario})

def cargar_corpo(request):
    
    if request.method ==  'POST':
        mi_formulario = Corpo(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            nuevo_corpo = Corporativos(empresa=informacion['empresa'], dia=informacion['dia'], costo=informacion['costo'])
            nuevo_corpo.save()
        return render(request, 'home.html')
    else:
        mi_formulario =Corpo()
    return render(request, 'cargar_corpo.html', {"mi_formulario":mi_formulario})

def cargar_turismo(request):

    if request.method ==  'POST':
        mi_formulario = Tourism(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            nuevo_turismo = Turismo(group=informacion['group'], date=informacion['date'], price=informacion['price'])
            nuevo_turismo.save()
        return render(request, 'home.html')
    else:
        mi_formulario =Tourism()
    return render(request, 'cargar_turismo.html', {"mi_formulario":mi_formulario})

def busqueda_wedding(request):
    return render(request, 'busqueda_wedding.html')

def buscar(request):
    if request.GET["name"]:
    #respuesta = f"Estoy buscando el casamiento de: {request.GET['name']}"
        name = request.GET['name']
        fechas = Weddings.objects.filter(name__icontains=name)
        return render(request, "resultadosbusqueda.html", {'name':name, 'fechas':fechas})

    else:
        respuesta = "No enviaste datos"

    return render(request,'home.html', {"respuesta":respuesta})

def busqueda_corpo(request):
    return render(request, 'busqueda_corpo.html')

def buscar_corpo(request):
    if request.GET["empresa"]:
    #respuesta = f"Estoy buscando el casamiento de: {request.GET['name']}"
        empresa = request.GET['empresa']
        dias = Corporativos.objects.filter(empresa__icontains=empresa)
        return render(request, "resultadoscorpo.html", {'empresa':empresa, 'dias':dias})

    else:
        respuesta = "No enviaste datos"

    return render(request,'home.html', {"respuesta":respuesta})

def busqueda_turismo(request):
    return render(request, 'busqueda_turismo.html')

def buscar_turismo(request):
    if request.GET["group"]:
    #respuesta = f"Estoy buscando el casamiento de: {request.GET['name']}"
        group = request.GET['group']
        dates = Turismo.objects.filter(group__icontains=group)
        return render(request, "resultadosturismo.html", {'group':group, 'dates':dates})

    else:
        respuesta = "No enviaste datos"

    return render(request,'home.html', {"respuesta":respuesta})