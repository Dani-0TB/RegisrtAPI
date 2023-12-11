from django.contrib import admin
from django.urls import path, include
from .views import RedirectRoot, ApiRoot

urlpatterns = [
    path('', RedirectRoot.as_view()),
    path('api/', ApiRoot.as_view(), name='api-root'),
    path('api/auth/', include('api.auth_service.urls')),
    path('api/asistencia/', include('api.asistencia.urls'))
]
