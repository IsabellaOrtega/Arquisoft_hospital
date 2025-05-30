from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import PruebaDiagnostica
from .forms import PruebaDiagnosticaForm
from usuarios.models import Paciente
from appBase.auth0backend import getRole
from django.contrib.auth.decorators import login_required

# Vista para listar todas las pruebas diagnósticas
@login_required
def lista_pruebas(request):
    role = getRole(request)
    if role == "Doctor":
        pruebas = PruebaDiagnostica.objects.all()
        mensaje = None
        if not pruebas.exists():
            mensaje = "No hay pruebas diagnósticas registradas en este momento."
        return render(request, 'listaPruebas.html', {'pruebas': pruebas, 'mensaje': mensaje})
    else:
        return HttpResponse("Unauthorized User")

# Vista para mostrar el detalle de una prueba diagnóstica
@login_required
def detalle_prueba(request, prueba_id):
    role = getRole(request)
    if role == "Doctor":
        prueba = get_object_or_404(PruebaDiagnostica, id=prueba_id)
        return render(request, 'detallePrueba.html', {'prueba': prueba})
    else:
        return HttpResponse("Unauthorized User")

# Vista para registrar una nueva prueba diagnóstica
@login_required
def nueva_prueba(request):
    role = getRole(request)
    if role == "Doctor":
        if request.method == 'POST':
            form = PruebaDiagnosticaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_pruebas')
        else:
            form = PruebaDiagnosticaForm()
        return render(request, 'nuevaPrueba.html', {'form': form})
    else:
        return HttpResponse("Unauthorized User")

# Vista para editar una prueba diagnóstica existente
@login_required
def editar_prueba(request, prueba_id):
    role = getRole(request)
    if role == "Doctor":
        prueba = get_object_or_404(PruebaDiagnostica, id=prueba_id)
        if request.method == 'POST':
            form = PruebaDiagnosticaForm(request.POST, instance=prueba)
            if form.is_valid():
                form.save()
                return redirect('detalle_prueba', prueba_id=prueba.id)
        else:
            form = PruebaDiagnosticaForm(instance=prueba)
        return render(request, 'editarPrueba.html', {'form': form, 'prueba': prueba})
    else:
        return HttpResponse("Unauthorized User")

# Vista para eliminar una prueba diagnóstica
@login_required
def eliminar_prueba(request, prueba_id):
    role = getRole(request)
    if role == "Doctor":
        prueba = get_object_or_404(PruebaDiagnostica, id=prueba_id)
        if request.method == 'POST':
            prueba.delete()
            return redirect('lista_pruebas')
        return render(request, 'eliminarPrueba.html', {'prueba': prueba})
    else:
        return HttpResponse("Unauthorized User")
