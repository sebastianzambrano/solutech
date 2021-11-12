from rest_framework import serializers
from authApp.models.incidencia import Incidencia


class IncidenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Incidencia
        fields = ['nom_equipo', 'ip', 'ambiente', 'sistema']


    def to_representation(self, obj):
        incidencia = Incidencia.objects.get(id=obj.id)

        return {
                    'nom_equipo': incidencia.id,
                    'ip': incidencia.username,
                    'ambiente': incidencia.name,
                    'sistema': incidencia.email,
                }