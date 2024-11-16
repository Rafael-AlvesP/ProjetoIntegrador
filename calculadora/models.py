from django.db import models
from django.db import models

class Prazo(models.Model):
    nomeEvento = models.CharField(max_length=100)
    processo = models.CharField(max_length=100)
    evento = models.CharField(max_length=100)
    dataPubli = models.DateField()
    prazoDias = models.CharField(max_length=10, default='8')
    notificar = models.CharField(max_length=1, choices=[('S', 'Sim'), ('N', 'Não')], default='N')
    dataFicto = models.DateField()
    dataFinal = models.DateField()

    def __str__(self):
        return self.nomeEvento

