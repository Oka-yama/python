# Utilizamos o while quando a repetição
# depende de uma condição ára ser finalizada

# O while significa enquanto, então podemos ler o código a seguir da seguinte forma enquanto o contador for menor ou igual a 5, mostre o contador e depois some 1 a ele

contador = 1
numero = 5
calculo = 0
while contador <= 5:
    calculo = contador + numero
    contador += 1


#1 Faça um programa que peça a senha de um usuário e compare com uma senha definida por você

senha = ''
while senha != 'papaia':
   senha = input('Digite a senha:')
   if senha == 'papaia':
       break
   print('acesso negado')
print('acesso permitido')

#2 Mantenha um menu aberto, até o usuário escolher sair

opcao = ''
while opcao != ('0'):
    print('\n ==== Menu ====')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Editar')
    print('0 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print('Opção cadastrar escolhida')
    elif opcao == '2':
        print('Opção listar escolhida')
    elif opcao == '3' :
        print('Opção editar escolhida')
    elif opcao == '0':
        print('Opção sair escolhida')
    else:
        print('Opção invalida')
