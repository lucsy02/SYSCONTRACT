from django.db import models
from django.utils import timezone




class Cliente(models.Model):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    instituicao_escolar = models.CharField(max_length=255)
    serie = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255)
    regiao = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    nome_responsavel = models.CharField(max_length=255)
    cpf_responsavel = models.CharField(max_length=14)
    rg_responsavel = models.CharField(max_length=12)
    email_responsavel = models.EmailField()
    telefone_responsavel = models.CharField(max_length=15)
    data_nascimento_responsavel = models.DateField()
    profissao_responsavel = models.CharField(max_length=255)
    sexo_responsavel = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_completo
