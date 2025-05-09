from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    

class Usuario(models.Model):
    ROL_OPCIONES = [('profesional', 'Profesional de la salud'),('paciente', 'Paciente'),]

    nombre = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rol = models.CharField( max_length=20,choices=ROL_OPCIONES, default='paciente')

    def __str__(self):
        return self.nombre + " - " + self.rol

class Paciente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pacientes')
    email = models.EmailField(max_length=100, unique=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.usuario.nombre
    
class ProfesionalSalud(models.Model):
    registro_medico = models.CharField(max_length=20, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='profesionales_salud')

class Doctor(models.Model):
    profesional_salud = models.ForeignKey(ProfesionalSalud, on_delete=models.CASCADE, related_name='doctores')
    especialidad = models.CharField(max_length=100)
    consultorio = models.CharField(max_length=100)

    def __str__(self):
        return self.professional_salud.usuario.nombre + " - " + self.especialidad

class Enfermero(models.Model):
    profesional_salud = models.ForeignKey(ProfesionalSalud, on_delete=models.CASCADE, related_name='enfermeros')
    area_especialidad = models.CharField(max_length=100)

class Tecnico(models.Model):
    profesional_salud = models.ForeignKey(ProfesionalSalud, on_delete=models.CASCADE, related_name='tecnicos')
    especialidad_examen = models.CharField(max_length=100)

class Cita(models.Model):
    doctor = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=200)
    numero_reserva = models.CharField(max_length=50, unique=True)
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('ocupado', 'Ocupado')])
    paciente = models.CharField(max_length=100, blank=True, null=True)  # Nombre del paciente que reserva

    def __str__(self):
        return f"{self.doctor} - {self.especialidad} ({self.fecha} {self.hora})"