from rest_framework import serializers
from .models import allObservations

class mySerializer(serializers.ModelSerializer):
    class Meta:
        model = allObservations
        fields = '__all__'
