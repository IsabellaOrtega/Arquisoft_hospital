# filepath: c:\Users\juanp\ProyectosVS\Arquisoft_hospital\pruebasDiagnosticas\forms.py
from django import forms
from .models import PruebaDiagnostica

class PruebaDiagnosticaForm(forms.ModelForm):
    class Meta:
        model = PruebaDiagnostica
        fields = ['paciente', 'historia_clinica', 'nombre', 'fecha_realizacion', 'resultados', 'comentarios']