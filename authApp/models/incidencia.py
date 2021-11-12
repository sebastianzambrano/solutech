from django.db import models


class Incidencia(models.Model):
    nom_equipo = models.CharField('nom_equipo', max_length= 20)
    ip = models.CharField('ip', max_length = 20)
    ambiente =  models.CharField('ambiente', max_length= 30)
    sistema =  models.CharField('Sistema', max_length=20)

    
    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural='Incidencias'


    def natural_key(self):
        return (self.nom_equipo)


    def _str_(self):
        return self.nom_equipo