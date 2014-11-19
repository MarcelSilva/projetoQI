from django import forms
from pessoas.models import Pessoa

class formPessoa(forms.ModelForm):
  class Meta:
      model = Pessoa
      
class formLogin(forms.Form):
	usuario_nome = forms.CharField(max_length = '15', required = True)
	usuario_nome = forms.CharField(max_length = '12', required = True)