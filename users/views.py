

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from backend.permissions import IsCreator

from users.models import PerfumesUser

from rest_framework.permissions import IsAuthenticated

from users.serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    CreateAPIView ensures only a create operation is possible
    """
    permission_classes = [AllowAny]
    queryset = PerfumesUser.objects.all()
    serializer_class = RegisterSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCreator]
    queryset = PerfumesUser.objects.all()
    serializer_class = UserSerializer
