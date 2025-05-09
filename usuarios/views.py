from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Cita, Project, Task, Doctor
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("hello world %s" % username)

def menu(request):
    return render(request,"menu.html")

def logIn(request):
    return render(request,"logIn.html")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request):
    return HttpResponse("tasks")

def doctores(request):
    doctors = list(Doctor.objects.values())
    return render(request, 'doctores.html', 
                {'doctores': doctors})

def citas_disponibles(request):
    # Filtrar solo las citas que están en estado "disponible"
    citas = Cita.objects.filter(estado='disponible')
    return render(request, 'citas_disponibles.html', {'citas': citas})

def reservar_cita(request, cita_id):
    # Obtener la cita por su ID
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        # Obtener el nombre del paciente del formulario
        paciente = request.POST['paciente']
        # Actualizar la cita con el nombre del paciente y cambiar el estado a "ocupado"
        cita.paciente = paciente
        cita.estado = 'ocupado'
        cita.save()
        # Redirigir a la página de citas disponibles
        return redirect('citas_disponibles')
    return render(request, 'reservar_cita.html', {'cita': cita})