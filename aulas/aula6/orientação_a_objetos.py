#Orientação a objetos é uma forma de organizar código aproximando a programação de elementos do mundo real

#Classe

#A classe funciona como um molde para criar objetos

class ContaBancaria:
    pass

#Objeto

#Objeto é uma instância da classe
#cada objeto poderá ter seus próprios dados

conta = ContaBancaria()
#titular, número da conta e saldo
#self.titular
#self.numero
#self.saldo

#Métodos

#Os métodos são as ações que o objeto pode executar

def depositar(self, valor):
    self.saldo += valor

#Herança de classe

#A herança permite criar uma nova classe a partir de outra já existente

class ContaCorrente(ContaBancaria):
    pass

#A classe ContaCorrente pode herdar características e comportamentos da classe ContaBancária.