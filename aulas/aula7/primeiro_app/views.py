#Importa a função HttpResponse do módulo django.http para criar respostas HTTP simples.
from django.http import HttpResponse

from django.shortcuts import render

from primeiro_app.forms import PerfilForm

# Create your views here.
# Define a view function chamada 'home' que recebe um objeto 'request' como argumento e retorna uma resposta Http
def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def criar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse('Perfil criado com sucesso')
    else:
        form = PerfilForm()
    return render(request, 'criar_perfil.html', {'form': form})