from django.shortcuts import render, HttpResponseRedirect
from pessoas.forms import cadastroPessoa, formPessoa

def index (request):
    form = formPessoa()
    return render(request,'index.html' ,{'form':form})

def cadastro(request):
    form = cadastroPessoa()
    return render(request, 'form_cadastroUsuario.html',{'form': form})
  
def salvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            pessoa = Pessoa.objects.get(pk=codigo)
        except:
            pessoa = Pessoa()

        pessoa.nome = request.POST.get('nome', '').upper()
        pessoa.email = request.POST.get('email', '').upper()
        pessoa.usuario = request.POST.get('usuario', '').upper()
        pessoa.senha = request.POST.get('senha', '').upper()

        pessoa.save()
    return HttpResponseRedirect('/pessoas/')


