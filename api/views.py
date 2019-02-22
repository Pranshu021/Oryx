from rest_framework import generics
from productapi.models import Smartphone, Rated
from .serializers import SmartphoneSerializers

class SmartphoneAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = SmartphoneSerializers
    
    def get_queryset(self):
        return Smartphone.objects.all();
    