from django.urls import path
from . import views
urlpatterns = [
    path("listarClases", views.ListarClases.as_view(), name="listar-clases"),
    path("crearListaAsistencia", views.CrearListaAsistencia.as_view(), name="crear-lista-asistencia"),
    path("mostrarLista", views.MostrarLista.as_view(), name="mostrar-lista"),
    path("confirmarAsistencia", views.ConfirmarAsistencia.as_view(), name="confirmar-asistencia")
]