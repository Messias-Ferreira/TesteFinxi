from django.db import models

# Create your models here.

class Endereco (models.Model):
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=254)
    bairro = models.CharField(max_length=254)
    cidade = models.CharField(max_length=254)
    uf = models.CharField(max_length=2)

class Imagens (models.Model):
    imagem1 = models.ImageField()
    imagem2 = models.ImageField(blank=True,null=True)
    imagem3 = models.ImageField(blank=True,null=True)
    imagem4 = models.ImageField(blank=True,null=True)

class Imoveis (models.Model):
    imagens = models.ForeignKey(Imagens,on_delete=models.CASCADE,default=1)
    endereco = models.OneToOneField(Endereco,on_delete=models.CASCADE,default=1)
    valor_aluguel = models.DecimalField(max_digits = 19,decimal_places=2)
    quartos = models.PositiveIntegerField()
    suites = models.PositiveIntegerField()
    iptu = models.DecimalField(max_digits = 19,decimal_places=2)
    condominio = models.DecimalField(max_digits = 19,decimal_places=2)
    descricao = models.TextField()
    

    
