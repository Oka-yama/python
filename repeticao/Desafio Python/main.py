
opcoes = ''
while opcoes != "7":
      print("\n======================================",
            "\nOpções:   | Funcionalidades:"
            "\n--- 1 --- | Cadastrar candidato/colaborador",
            "\n--- 2 --- | Listar todos os cadastros",
            "\n--- 3 --- | Buscar uma pessoa pelo nome",
            "\n--- 4 --- | Alterar uma informação cadastrada",
            "\n--- 5 --- | Remover uma pessoa da lista",
            "\n--- 6 --- | Exibir resumo do processo seletivo",
            "\n--- 7 --- | Sair do sistema")
      opcoes = input('Selecione uma opção: ')
      if opcoes > '7':
          print('Opção inválida')

cadastro = {
    "Nome": input('Insira seu nome: '),
    "Idade": input('Insira sua idade: '),
    "Cargo pretendido": input('Insira o cargo pretendido: '),
    "Salário desejado": input('Insira o salário desejado: '),
    "Status do processo": input('Insira o status processo: ')
    }
print(cadastro)