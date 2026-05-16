class ContaBancaria():
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self. extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior do que zero")
            return
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print("O valor do depósito foi realizado com sucesso")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior do que zero")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
            return

        self.saldo -= valor
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        print("O saque foi realizado com sucesso")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("O valor da transferência deve ser maior do que zero")
            return

        if valor > self.saldo:
            print("Saldo insuficiente para transferir.")
            return
        self.saldo -= valor
        conta_destino.saldo += valor
        self.extrato.append(f"Tranferência enviada R$: {valor:.2f} para {conta_destino.titular}")
        conta_destino.extrato.append(f"Transfência recebida R$ {valor:.2f} de {self.titular}")
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso")

    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: {self.saldo:.2f}")

    def exibir_extrato(self):
        print(f"\nExtrato da conta de {self.titular}")
        print("-" * 30)

        if not self.extrato:
            print("Nenhuma movimentação realizada")
        else:
            for operaçao in self.extrato:
                print(operaçao)
        print("-" * 30)
        print(f"Saldo final: R$ {self.saldo:.2f}")

    def ___str___(self):
        return f"Conta {self.titular}: {self.numero_conta} | Titular: {self.titular} | Saldo: {self.saldo:.2f} R${valor:.2f} para {conta_destino.titular}"

conta1 = ContaBancaria("Bryan","001", 1000)
conta2 = ContaBancaria("Bruno", "002", 500)
print(conta1)
print(conta2)

conta1.depositar(1000)
conta1.sacar(250)
conta1.transferir(150, conta2)

conta1.consultar_saldo()
conta2.consultar_saldo()

conta1.exibir_extrato()
conta2.exibir_extrato()