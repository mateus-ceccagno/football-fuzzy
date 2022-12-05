from django.db import models

# Create your models here.
class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    vitorias = models.IntegerField()
    touchdowns = models.IntegerField()
    jardas = models.IntegerField()
    recepcoes = models.IntegerField()
    resultado = models.FloatField(blank=True)
