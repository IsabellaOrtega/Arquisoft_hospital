from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('menu/', views.menu),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks), 
    path('doctores/', views.doctores),
    path('citas/disponibles/', views.citas_disponibles, name='citas_disponibles'),
    path('citas/reservar/<int:cita_id>/', views.reservar_cita, name='reservar_cita'),

]
