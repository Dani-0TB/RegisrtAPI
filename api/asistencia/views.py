from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from . import models
from .serializers import ProfesorSerializer, AlumnoSerializer

class ListarClases(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        profesor = get_object_or_404(models.Profesor, user = user)
        if not user:
            return Response({"detail": "Not Found"}, status.HTTP_404_NOT_FOUND)
        secciones = models.Seccion.objects.filter(profesor = profesor)
        response = {"clases":[]}
        for seccion in secciones:
            clases = models.Clase.objects.filter(seccion=seccion)
            for clase in clases:
                response["clases"].append({"id": clase.pk, "nombre": clase.__str__()})
        return Response(response, status.HTTP_200_OK)

class CrearListaAsistencia(APIView):
    def post(self, request):
        id_clase = request.data["idClase"]
        if not id_clase:
            return Response({"detail":"Not found."})
        try:
            clase = models.Clase.objects.get(pk = id_clase)
            seccion = models.Seccion.objects.get(pk = clase.seccion.pk)
            listaAlumnos = models.SeccionAlumno.objects.filter(seccion = seccion)
            for seccionAlumno in listaAlumnos:
                asistencia = models.Asistencia(clase = clase, alumno = seccionAlumno.alumno)
                asistencia.save()
        except Exception as e:
            return Response({"detail":str(e)}, status.HTTP_400_BAD_REQUEST)
        return Response({"detail":"Asistencia creada con exito"}, status.HTTP_201_CREATED)

import datetime

class MostrarLista(APIView):
    def post(self,request):
        id_clase = request.data["idClase"]
        if not id_clase:
            return Response({"detail":"Not found."})
        try:
            clase = models.Clase.objects.get(pk = id_clase)
            fecha = datetime.date.today()
            response = {"listaAlumnos":[]}
            listaAlumnos = models.Asistencia.objects.filter(clase = clase, fecha = fecha)
            for alumno in listaAlumnos:
                response["listaAlumnos"].append(
                    {
                        "nombre": f"{alumno.alumno.user.first_name} {alumno.alumno.user.last_name}",
                        "presente": f"{alumno.presente}"
                    }
                )
            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail":str(e)}, status.HTTP_400_BAD_REQUEST)

class ConfirmarAsistencia(APIView):
    def post(self,request):
        id_clase = request.data["idClase"]
        if not id_clase:
            return Response({"detail":"Not found."})
        try:
            clase = models.Clase.objects.get(pk = id_clase)
            fecha = datetime.date.today()
            user = models.User.objects.get(username = request.data["username"])
            alumno = models.Alumno.objects.get(user=user)
            asistenciaAlumno = models.Asistencia.objects.get(clase = clase, fecha = fecha, alumno=alumno)
            if asistenciaAlumno.presente:
                return Response({"detail":"Alumno ya está presente"})
            else:
                asistenciaAlumno.presente = True
                asistenciaAlumno.save()
                return Response({"detail":"El alumno fue colocado presente"}, status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail":str(e)}, status.HTTP_400_BAD_REQUEST)