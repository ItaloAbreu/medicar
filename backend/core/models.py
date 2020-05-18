from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=64)
    crm = models.IntegerField()
    email = models.EmailField(max_length=254,)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} (CRM: {self.crm})'
