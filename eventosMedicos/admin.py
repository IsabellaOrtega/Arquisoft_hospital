from django.contrib import admin

# Register your models here.
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'especialidad', 'fecha', 'hora', 'estado')