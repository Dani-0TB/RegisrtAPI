from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from . import models
from .serializers import ProfesorSerializer, AlumnoSerializer

class ListarProfesores(APIView):
    def get(self,request):
        qs = models.Profesor.objects.all()
        serializer = ProfesorSerializer(qs, many=True)
        return Response(serializer.data)

class ListarAlumnos(APIView):
    def get(self,request):
        qs = models.Alumno.objects.all()
        serializer = AlumnoSerializer(qs, many=True)
        return Response(serializer.data)