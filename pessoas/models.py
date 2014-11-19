from django.db import models



class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  email = models.EmailField()
  usuario = models.CharField(max_length=15)
  senha = models.CharField(max_length=12)
  
class frm_Login(models.Model):
  usuario = models.CharField(max_length = 15)
  senha = models.CharField(max_length = 12)
  