from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Alumno)
admin.site.register(models.Profesor)
admin.site.register(models.Ramo)
admin.site.register(models.Seccion)
admin.site.register(models.SeccionAlumno)
admin.site.register(models.Clase)
admin.site.register(models.Asistencia)