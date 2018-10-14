from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserDetailSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


@api_view(['GET'])
def curent_user(request):
    if request.user.is_authenticated:
        return Response({"username": request.user.username})
    return Response({"detail": "AnonymousUser. Login please."})