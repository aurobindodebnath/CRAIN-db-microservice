from rest_framework import serializers
from .models import appsecObservation, vaptObservation, vaptPlugin, scrObservation

class appsecSerializer(serializers.ModelSerializer):
    class Meta:
        model = appsecObservation
        fields = '__all__'

class vaptSerializer(serializers.ModelSerializer):
    class Meta:
        model = vaptObservation
        fields = '__all__'

class scrSerializer(serializers.ModelSerializer):
    class Meta:
        model = scrObservation
        fields = '__all__'

class vaptPluginSerializer(serializers.ModelSerializer):
    vapt_observation = vaptSerializer()
    class Meta:
        model = vaptPlugin
        fields = ['pluginID','vapt_observation']