from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    altura = models.FloatField()
    peso = models.FloatField()   

    def __str__(self):
        return self.nome
