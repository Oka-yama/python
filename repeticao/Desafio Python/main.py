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
    print("--- SISTEMA DE CADASTRO DE CANDIDATOS ---")
    print(" (Opções: | Funcionalidades:")
    print("--- 1 --- | Cadastrar candidato/colaborador")
    print("--- 2 --- | Listar todos os cadastros")
    print("--- 3 --- | Buscar uma pessoa pelo nome")
    print("--- 4 --- | Alterar uma informação cadastrada")
    print("--- 5 --- | Remover uma pessoa da lista")
    print("--- 6 --- | Exibir resumo do processo seletivo")
    print("--- 7 --- | Sair do sistema")

def cadastrar_pessoas():
    print("\n--- Cadastro de candidato/colaborar ---")
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
        "status": status
    }

    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def buscar_pessoas():
    print("\n--- Buscar pessoa pelo nome ---")

    if len(pessoas) == 0:
        print('Nenhuma pessoa cadastrada')
        return

    for indice, pessoa in enumerate(pessoas, start=1):
        print(f"\n Cadastro {indice}")
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"Cargo pretendido: {pessoa['cargo']}")
        print(f"Salário desejado: {pessoa['salario']:.2f}")
        print(f"Status: {pessoa['status']}")
    nome_busca = input("Digite o nome para buscar: ").strip().lower()
    encontrou = False
    for pessoa in pessoas:
        if pessoa["nome"].lower() == nome_busca:
            print('Pessoa encontrada!')
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Cargo pretendido:"
                  f" {pessoa['nome']}")
            print(f"Salário pretendido: {pessoa['salario']}")
            print(f"Status: {pessoa['status']}")
            encontrou = True
            break

    if not encontrou:
        print('Pessoa não encontrada!')