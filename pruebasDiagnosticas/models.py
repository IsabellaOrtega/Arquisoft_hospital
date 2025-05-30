# filepath: c:\Users\juanp\ProyectosVS\Arquisoft_hospital\pruebasDiagnosticas\models.py
from django.db import models
from usuarios.models import Paciente
from reportes.models import HistoriaClinica

class PruebaDiagnostica(models.Model):
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name='pruebas_diagnosticas'
    )
    historia_clinica = models.ForeignKey(
        HistoriaClinica, on_delete=models.SET_NULL, null=True, blank=True, related_name='pruebas_diagnosticas'
    )
    nombre = models.CharField(max_length=100)
    fecha_realizacion = models.DateField()
    resultados = models.TextField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.paciente.usuario.nombre} ({self.fecha_realizacion})"