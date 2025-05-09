from django.urls import path
from . import views

urlpatterns = [
    path('citas/agendar', views.agendar_cita, name='agendar_cita'),
    path('citas/disponibilidad', views.revisar_disponibilidad, name='revisar_disponibilidad'),
    path('citas/crear', views.crear_cita, name='crear_cita'),
    path('citas/manejar', views.manejar_citas, name='manejar_citas'),
    path('citas/consultar', views.consultar_citas, name='consultar_citas'),
    path('historial/consultar', views.consultar_historial, name='consultar_historial'),
    path('laboratorio/resultados', views.resultados_laboratorio, name='resultados_laboratorio'),
    path('telemedicina', views.telemedicina, name='telemedicina'),
    path('vacunacion', views.vacunacion, name='vacunacion'),
    path('atencion-domiciliaria', views.atencion_domiciliaria, name='atencion_domiciliaria'),
]