from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f'Especialidade - {nome}'
