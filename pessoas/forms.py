from django import forms
from pessoas.models import Pessoa

class formPessoa(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
      model = Pessoa
      
class cadastroPessoa(models.Model):
  nome = models.CharField(max_length=100, required=True)
  email = models.EmailField()
  usuario = models.CharField(max_length=15, required=True)
  senha = models.CharField(wudget=forms.PasswordInput, required=True)
  
class frm_Login(models.Model):
  usuario = models.CharField(max_length =15, required=True)
  senha = models.CharField(max_length =12, required=True)