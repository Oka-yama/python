#Cadastrar candidato ou colaborador
#Listar todos os candidatos
#Buscar uma pessoa pelo nome
#Alterar uma informação cadastrada
#Remover uma pessoa da lista
#Exibir um resumo do processo seletivo
#Sair do sistema

status_permitidos = ('Em análise', "Aprovado", "Reprovado", "Contratado")

pessoas = []

def mostrar_menu():
    print("\n--- SISTEMA DE CADASTRO DE CANDIDATOS ---")
    print(" Opções:  | Funcionalidades:")
    print("--- 1 --- | Cadastrar candidato/colaborador")
    print("--- 2 --- | Listar todos os cadastros")
    print("--- 3 --- | Buscar uma pessoa pelo nome")
    print("--- 4 --- | Alterar uma informação cadastrada")
    print("--- 5 --- | Remover uma pessoa da lista")
    print("--- 6 --- | Exibir resumo do processo seletivo")
    print("--- 7 --- | Sair do sistema")

def cadastrar_pessoas():
    print("\n--- Cadastro de candidado/colaborar ---")
    nome = input("Nome: ").strip()
    if nome == "":
        print("O nome não pode ser vazio")
        return

    for pessoa in pessoas:
        if pessoa["nome"].lower() == nome.lower():
            print("Já existe uma pessoa com esse nome")
            return

    try:
        idade = int(input("Idade: "))
        salario = float(input("Salário desejado: "))
    except:
        print("Idade e salário precisam ser valores numéricos")
        return

    cargo = input("Cargo pretendido: ").strip()
    if cargo == "":
        print("O cargo não pode ser vazio")
        return

    print("\n Status permitidos: ")
    for status in status_permitidos:
        print(f"-{status}")

    status = input("Status do processo: ").strip()

    if status not in status_permitidos:
        print("Status inválido.")
        return

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cargo": cargo,
        "salario": salario,
        "status": status
    }

    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")


def listar_pessoas():
    print("\n --- Lista de cadastros ---")

    if (len(pessoas)) == 0:
        print("Nenhuma pessoa cadastrada")
        return

    for indice, pessoa in enumerate(pessoas, start=1):
        print(f"\n Cadastro {indice}")
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"Cargo pretendido: {pessoa['cargo']}")
        print(f"Salário desejado: {pessoa['salario']:.2f}")
        print(f"Status: {pessoa['status']}")


def buscar_pessoa():
    print("\n --- Buscar pessoa pelo nome ---")

    if (len(pessoas)) == 0:
        print("Nenhuma pessoa cadastrada")
        return

    nome_busca = input("Digite o nome para buscar: ").strip().lower()

    encontrou = False
    for pessoa in pessoas:
        if pessoa['nome'].lower() == nome_busca:
            print("Pessoa encontrada!")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Cargo pretendido: {pessoa['cargo']}")
            print(f"Salário desejado: {pessoa['salario']:.2f}")
            print(f"Status: {pessoa['status']}")
            encontrou = True
            break

    if not encontrou:
        print("Pessoa não encontrada")


def alterar_pessoa():
    print("\n --- Alterar informação cadastrada ---")

    if (len(pessoas)) == 0:
        print("Nenhuma pessoa cadastrada")
        return

    nome_busca = input("Digite o nome para buscar: ").strip().lower()

    encontrou = False
    for pessoa in pessoas:
        if pessoa['nome'].lower() == nome_busca:
            print("Pessoa encontrada!")
            print("Qual informação deseja alterar")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Cargo pretendido")
            print("4 - Salário desejado")
            print("5 - Status do processo")

            opcao = input("Escolha uma opção")

            if opcao == "1":
                novo_nome = input("Novo nome: ").strip()
                if novo_nome == "":
                    print("O nome não pode ser vazio")
                    return

                pessoa['nome'] = novo_nome

            elif opcao == "2":
                try:
                    nova_idade = int(input("Nova idade: ").strip())
                    pessoa['idade'] = nova_idade
                except ValueError:
                    print("Idade inválida.")
                    return

            elif opcao == "3":
                novo_cargo = input("Novo cargo pretendido: ").strip()
                if novo_cargo == "":
                    print("O cargo não pode ser vazio")
                    return

                pessoa['cargo'] = novo_cargo

            elif opcao == "4":
                try:
                    novo_salario = float(input("Novo salario: ").strip())
                    pessoa['salario'] = novo_salario
                except ValueError:
                    print("Salário inválida.")
                    return

            elif opcao == "5":
                print("\n Status permitidos: ")
                for status in status_permitidos:
                    print(f"-{status}")

                novo_status = input("Novo status : ").strip()
                if novo_status not in status_permitidos:
                    print("Status inválido.")
                    return

                pessoa['status'] = novo_status

            else:
                print("Opção inválida.")
                return
            print("Informação alterada com sucesso!")
            return

        print("Pessoa não encontrada")

def remover_pessoa():
    print("\n --- Remover pessoa da lista ---")

    if (len(pessoas) == 0):
        print("Nenhuma pessoa na lista")
        return

    nome_busca = input("Digite o nome da pessoa que quer remover: ").strip().lower()

    for pessoa in pessoas:
        if pessoa['nome'].lower() == nome_busca:
            pessoas.remove(pessoa)
            print("Pessoa removida com sucesso!")
            return

    print("Pessoa não encontrada")

def exibir_resumo():
    print("\n --- Resumo do processo seletivo ---")

    if (len(pessoas) == 0):
        print("Nenhuma pessoa cadastrada")
        return

    print(f"Total de pessoas cadastradas: {len(pessoas)}")

    for status in status_permitidos:
        contador = 0
        for pessoa in pessoas:
            if pessoa['status'] == status:
                contador += 1
            print(f"{status}: {contador}")

while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_pessoas()

    elif opcao == "2":
        listar_pessoas()

    elif opcao == "3":
        buscar_pessoa()

    elif opcao == "4":
        alterar_pessoa()

    elif opcao == "5":
        remover_pessoa()

    elif opcao == "6":
        exibir_resumo()

    elif opcao == "7":
        print("Sistema encerrado")
        break