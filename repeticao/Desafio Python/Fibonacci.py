# Crie uma função chamada gerar Fibonacci que receba como parâmetro a quantidade de termos que deve ser exibidos:
from repeticao.aulas.input import quantidade

# O programa de verá solicitar ao usuário a quantidade de termos exibida.
# A função deverá receber um número inteiro como parâmetro.
# A função de exibir a sequência de Fibonacci até a quantidade informada.
# Caso o usuário digite um número menor ou igual a 0 o programa deverá exibir uma mensagem de erro.

def gerar_fibonacci():
    pri_num = 0
    seg_num = 1
    proximo_num = pri_num + seg_num
    pri_num = seg_num
    seg_num = pri_num
    contador = input(int("Insira a quantidade de números a ser exibida: "))

