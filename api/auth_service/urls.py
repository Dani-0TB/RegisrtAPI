from django.urls import path
from .views import Registrar, Login

urlpatterns = [
    path('login', Login.as_view(), name='auth-login'),
    path('registrar', Registrar.as_view(), name='auth-registrar'),
    
]