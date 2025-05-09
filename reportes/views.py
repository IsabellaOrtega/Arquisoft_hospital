from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import HistoriaClinica
from django.shortcuts import render, get_object_or_404
from usuarios.models import Paciente
from appBase.auth0backend import getRole
from django.contrib.auth.decorators import login_required

from .utils import retry_operation
# Create your views here.

@login_required
@retry_operation(max_retries=5, delay=2, exponential_backoff=True)
def consultaPaciente(request, paciente_id):
    role = getRole(request)
    if role == "Doctor":
        try:
        
            #consultaPaciente: Vista para consultar la historia clínica de un paciente.
            # Obtener el paciente por su ID
            paciente = get = get_object_or_404(Paciente, id=paciente_id)
            historiaClinica = paciente.historias_clinicas.all()
        
            data = {
                'paciente': paciente,
                'historiaClinica': historiaClinica,
            }

            return render(request, 'consultaPaciente.html', data)
        except Exception as e:
            # Manejo de errores
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def menuDoctor(request):
    role = getRole(request)
    if role == "Doctor":
        nombreDoc = request.user.username
        # Renderizar la plantilla del menú del doctor
        return render(request, 'menuConsulta.html')
    else:
        return HttpResponse("Unauthorized User")

@login_required
def pacientes(request):
    role = getRole(request)
    if role == "Doctor":
        # Obtener todos los pacientes
        pacientes = Paciente.objects.all()
    
        # Renderizar la plantilla con la lista de pacientes
        return render(request, 'pacientes.html', {'pacientes': pacientes})
    else:
        return HttpResponse("Unauthorized User")
