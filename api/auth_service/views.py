from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer

class Registrar(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            nuevo_user = User.objects.filter(username=request.data['username']).first()
            nuevo_user.set_password(request.data['password'])
            nuevo_user.save()
            token = Token.objects.create(user=nuevo_user)
            return Response({"user":serializer.data, "token": token.key}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        user = get_object_or_404(User, username=request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response({"detail": "Not Found"}, status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"user":request.data["username"],"token": token.key}, status.HTTP_202_ACCEPTED)

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AutenticarToken(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    def get(self, request):
        return Response({f"passed for {request.user.email}"})