from abc import ABC, abstractclassmethod #Para utilizar classes e métodos abstratos, eu preciso importar bibliotecas

class Animal(ABC): #herdando de ABC, Animal é uma classe abstrata
    def correr(self):
        print("Correr")
    
    @abstractclassmethod #estou obrigando os filhos a implementar o método respirar
    def respirar(self):
        print("Respirar")


class Cao(Animal):
    def respirar(self):
        print("Respirar como um cão")


class Passaro(Animal):
    def respirar(self):
        print("Respirar como um passaro")


#não posso criar uma instância de Animal dessa forma pois é uma classe abstrata
#animal = Animal()
#animal.correr()

cao = Cao()
cao.respirar() #Se não implementar respirar dentro de cão, devido ao decorator indicando isso, o código apresentara erro.
print(" ")

"""----------------------------------"""
class Conta(ABC):
    def __init__(self, numero_conta, saldo) -> None:
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        print(self._saldo)
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def depositar(self, valor):
        if valor>0:
            self._saldo += valor

    @abstractclassmethod #deve ser implementada nas classes filhas 
    def sacar(self,valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero_conta, saldo) -> None:
        super().__init__(numero_conta, saldo)
    
    def sacar(self,valor):
        limite = 1000
        if valor <= limite:
            self._saldo -= valor
        else:
            print(f"Limite de saque exedido: Limite: {limite}")


class ContaPoupança(Conta):
    def __init__(self, numero_conta, saldo) -> None:
        super().__init__(numero_conta, saldo)

    def sacar(self,valor):
        limite = 300
        if valor <= limite:
            self._saldo -= valor
        else:
            print(f"Limite de saque exedido: Limite: {limite}")


cc = ContaCorrente(1, 300)
cp = ContaPoupança(2, 400)

cc.saldo = 10000 #implementação possível devido ao decorator @saldo.setter
cc.sacar(399)
cc.saldo #impressão possível devido ao decorator @property
cp.sacar(400)
cp.saldo