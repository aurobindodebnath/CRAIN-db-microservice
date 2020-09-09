from django.shortcuts import render
from rest_framework import viewsets, status
from .models import appsecObservation, vaptPlugin, vaptObservation
from .serializers import appsecSerializer, vaptPluginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class appsecViewSet(viewsets.ModelViewSet):
    queryset = appsecObservation.objects.all()
    serializer_class = appsecSerializer

@api_view(['POST'])
def sendVAPTObs(request):
    if request.method == "POST":
        requested_plugins = request.data["plugins"]
        requested_observations = vaptPlugin.objects.filter(pluginID__in=requested_plugins)
        serialied_obs = vaptPluginSerializer(requested_observations, many = True)
        return Response(serialied_obs.data)
    return Response({"error": "Incorrect method"})