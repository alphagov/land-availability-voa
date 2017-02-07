from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import PropertySerializer
from .models import Property


class VOACreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
