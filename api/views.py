from django.shortcuts import render
from rest_framework import viewsets
from .models import allObservations
from .serializers import mySerializer

# Create your views here.

class appsecViewSet(viewsets.ModelViewSet):
    queryset = allObservations.objects.filter(ptype="Application Security")
    serializer_class = mySerializer

class networkViewSet(viewsets.ModelViewSet):
    queryset = allObservations.objects.filter(ptype="Network Architecture Review")
    serializer_class = mySerializer

class vaViewSet(viewsets.ModelViewSet):
    queryset = allObservations.objects.filter(ptype="Vulnerability Assessment")
    serializer_class = mySerializer

class mobsecViewSet(viewsets.ModelViewSet):
    queryset = allObservations.objects.filter(ptype="Mobile Application Security")
    serializer_class = mySerializer
