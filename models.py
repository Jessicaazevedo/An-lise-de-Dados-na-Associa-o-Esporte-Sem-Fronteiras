# jovens/models.py

from django.db import models

class Jovem(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    escolaridade = models.CharField(max_length=50)
    data_participacao = models.DateField()
    desempenho = models.FloatField()  # Altere o tipo para armazenar a pontuação numérica

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    jovem = models.ForeignKey(Jovem, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    nota = models.FloatField()

    def __str__(self):
        return f'{self.descricao} - {self.jovem.nome}'
