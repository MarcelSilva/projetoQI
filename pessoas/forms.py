from django import forms
from pessoas.models import Pessoa

class formPessoa(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
      model = Pessoa
      
class cadastroPessoa(forms.Form):
  nome = forms.CharField(max_length=100, required=True)
  email = forms.EmailField()
  usuario = forms.CharField(max_length=15, required=True)
  senha = forms.CharField(widget=forms.PasswordInput, required=True)
  
#class frm_Login(forms.Form):
  #usuario = forms.CharField(max_length =15, required=True)
  #senha = forms.CharField(widget=forms.PasswordInput, required=True)