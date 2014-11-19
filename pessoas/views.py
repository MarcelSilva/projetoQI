from django.shortcuts import render
from pessoas.forms import formPessoa

def index (request):
    form = formPessoa()
    return render(request,'index.html' ,{'form':form})


def validar (request):
	if request.method == 'POST':
		form = formPessoa(request.POST)

		if form.is_valid():
			form = Pessoa(**form.cleaned_data)
			pessoa.save()

			pessoas = Pessoa.objects.all()
			return render(request,'validar.html' ,{'form':form, 'pessoas':pessoas})

def tela_login():
	frm_login = frmLogin()
	return render(request,'form_login.html',{'frm_login':frm_login})