from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import PropertySerializer
from .models import Property


class VOACreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class VOADetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'ba_reference_number'
    lookup_url_kwarg = 'ba_ref'
