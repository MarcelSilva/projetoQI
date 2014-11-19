from django import forms
from pessoas.models import Pessoa

class formPessoa(forms.ModelForm):
  class Meta:
      model = Pessoa
     

   
    