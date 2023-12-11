from django.urls import path
from .views import ListarProfesores, ListarAlumnos

urlpatterns = [
    path('profesoresList', ListarProfesores.as_view(), name='profesores-list'),
    path('alumnosList', ListarAlumnos.as_view(), name='alumnos-list'),
]