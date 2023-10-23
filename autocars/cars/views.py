from django.shortcuts import render
from rest_framework import generics
from .models import Cars
from .serializer import CarsSerializer

class CarList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

