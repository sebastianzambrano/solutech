from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import serializers, status, views, generics
from rest_framework.response import Response
from authApp.models.incidencia import Incidencia
from authApp.serializers.incidenciaSerializer import IncidenciaSerializer

class IncidenciaCreateView(generics.CreateAPIView):
    queryset=Incidencia.objects.all()
    serializers_class=IncidenciaSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class IncidenciaView(generics.RetrieveAPIView):
    queryset=Incidencia.objects.all()
    serializers_class=IncidenciaSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class IncidenciaDetailView(generics.ListAPIView):
    queryset=Incidencia.objects.all()
    serializers_class=IncidenciaSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class IncidenciaUpdateView(generics.UpdateAPIView):
    queryset=Incidencia.objects.all()
    serializers_class=IncidenciaSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class IncidenciaDeleteView(generics.DestroyAPIView):
    queryset=Incidencia.objects.all()
    serializers_class=IncidenciaSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

