from django.shortcuts import render
from pessoas.forms import formPessoa

def index (request):
    form = formPessoa()
    return render(request,'index.html' ,{'form':form})
