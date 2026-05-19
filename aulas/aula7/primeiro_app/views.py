#Importa a função HttpResponse do módulo django.http para criar respostas HTTP simples.
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# Define a view function chamada 'home' que recebe um objeto 'request' como argumento e retorna uma resposta Http
def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')