#1 Crie um programa que mostre os números pares de 1 até 20

num1 = 1
while num1 != 20:

    if num1 % 2 == 0:
        print(num1)
    num1 += 1




#2 Peça 4 notas e calcule a média utilizando for ou while
media = 0
notas = 0
for notas in range(0,4):

    notaAtual = input('Digite um nota: ')
    media = int(notaAtual)
    notas += 1
    media / 4

print(media)

#3 Peça a idade de um usuário. Enquanto ele digitar uma idade negativa, solicite novamente

idade = -1
while idade < 0:
    idade = int(input('Digite a idade: '))