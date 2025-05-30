from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pruebas, name='lista_pruebas'),
    path('<int:prueba_id>/', views.detalle_prueba, name='detalle_prueba'),
    path('nueva/', views.nueva_prueba, name='nueva_prueba'),
    path('<int:prueba_id>/editar/', views.editar_prueba, name='editar_prueba'),
    path('<int:prueba_id>/eliminar/', views.eliminar_prueba, name='eliminar_prueba'),
]