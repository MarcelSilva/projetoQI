from django.shortcuts import render, HttpResponseRedirect
from pessoas.forms import cadastroPessoa, formPessoa

def index (request):
    form = formPessoa()
    return render(request,'index.html' ,{'form':form})

def cadastro(request):
    form = cadastroPessoa()
    return render(request, 'form_cadastroUsuario.html',{'form': form})
  
def validar (request):
	if request.method == 'POST':
		form = formPessoa(request.POST)

		if form.is_valid():
			form = Pessoa(**form.cleaned_data)
			pessoa.save()

			pessoas = Pessoa.objects.all()
			return render(request,'form_cadastroUsuario.html' ,{'form':form, 'pessoas':pessoas})

