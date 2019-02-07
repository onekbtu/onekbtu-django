from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from authentication.serializers import UserSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
