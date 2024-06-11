"""
Notações de nomes e variáveis
Pascal Case:   ContaBancaria
Camel Case:    contaBancaria
Snake Case:    conta_bancaria 
"""

#classes utilizam notação Pascal Case
class ContaBancaria:
    pass #pass cria um bloco vazio

class Conta:
    #criando um construtor
    def __init__(self, nome, saldo) -> None:
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor


conta = ContaBancaria() #criando uma instância de um objeto

conta2 = Conta("Patrik", 1000)
print(f"{conta2.nome}: {conta2.saldo}")
conta2.depositar(334)
print(f"{conta2.nome}: {conta2.saldo}")
conta2.sacar(140)
print(f"{conta2.nome}: {conta2.saldo}")