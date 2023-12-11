from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from . import models

class UserDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfesorSerializer(ModelSerializer):
    user = UserDataSerializer()
    class Meta:
        model = models.Profesor
        fields = ['rut','dvrut', 'user']

class AlumnoSerializer(ModelSerializer):
    user = UserDataSerializer()
    class Meta:
        model = models.Alumno
        fields = ['rut','dvrut', 'user']