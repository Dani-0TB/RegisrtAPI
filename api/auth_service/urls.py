from django.urls import path
from .views import Registrar, Login, GetNombreCompleto

urlpatterns = [
    path('login', Login.as_view(), name='auth-login'),
    path('registrar', Registrar.as_view(), name='auth-registrar'),
    path('getNombreCompleto', GetNombreCompleto.as_view(), name='auth-nombre-completo')
]