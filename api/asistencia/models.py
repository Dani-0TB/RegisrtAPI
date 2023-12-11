from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.IntegerField()
    dvrut = models.CharField(max_length=1)

    def __str__(self):
        return f"Alumno {self.user.first_name}"

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.IntegerField()
    dvrut = models.CharField(max_length=1)
    def __str__(self):
        return f"Profesor {self.user.first_name}"

class Ramo(models.Model):
    nombre = models.CharField(max_length=120)
    cupos = models.IntegerField(default=20, blank=True, null=False)
    def __str__(self):
        return f"{self.nombre}"

class Seccion(models.Model):
    profesor = models.OneToOneField(Profesor, on_delete=models.CASCADE)
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.ramo.nombre} S{self.pk} | Profesor: {self.profesor.user.first_name} {self.profesor.user.last_name}"

class SeccionAlumno(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.seccion.ramo.nombre} S{self.seccion.pk}"

class Clase(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    dia = models.CharField( max_length = 30, 
                            default='Lunes', 
                            choices=(('lun', 'Lunes'), 
                                    ('mar', 'Martes'), 
                                    ('mie', 'Miercoles'), 
                                    ('jue','Jueves'), 
                                    ('vie','Viernes'), 
                                    ('sab','Sabado'))
                        )
    hora_inicio = models.TimeField(_("Hora de inicio"))
    hora_termino = models.TimeField(_("Hora de termino"))
    def __str__(self):
        return f"{self.seccion.ramo.nombre} Seccion {self.seccion.pk} | {self.dia} de {self.hora_inicio.hour}:{self.hora_inicio.minute} a {self.hora_termino.hour}:{self.hora_termino.minute}"

class Asistencia(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"Asistencia de {self.alumno.user.first_name} {self.alumno.user.last_name} a {self.clase.seccion.ramo.nombre} {self.fecha}"
    

