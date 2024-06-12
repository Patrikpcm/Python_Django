"""
Polimorfismo: Qualidade ou estado de ser capaz de assumir diferentes formas
Poli -> muitas
morfo-> forma
"""

class Animal: #superclasse ou classe pai
    def __init__(self, cor, tamanho, peso) -> None:
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso

    def correr(self):
        print("correr como um", end=" ")

    def dormir(self):
        print("dormir")

    def __str__(self):
        return f'cor:{self.cor}, tamanho:{self.tamanho}, peso: {self.peso}'


class Cao(Animal): #subclasse ou classe filha
    def __init__(self, cor, tamanho, peso, raca="SRD") -> None: #adicionando um atributo específico de cão
        super().__init__(cor, tamanho, peso)
        self.peso = f'{peso}Kg' #sobrescrevendo um atributo já existente
        self.raca = raca

    def latir(self):
        print("latir")
    
    def correr(self):#sobrescrita de método (override)
        super().correr() #chamando a classe pai
        print("cão!")

    def __str__(self): #sobrescrevendo o método
        return super().__str__() + f', raca:{self.raca}'

class Passaro(Animal):#subclasse ou classe filha
    def __init__(self, cor, tamanho, peso) -> None:
        super().__init__(cor, tamanho, peso)

    def voar(self):
        print("voar")

    #def correr(self):
     #   super().correr()
      #  print("passaro")


class Papagaio(Passaro, Cao): #exemplo de herança múltipla
    def __init__(self, cor, tamanho, peso) -> None:
        super().__init__(cor, tamanho, peso)

    def correr(self):#sobrescrita de método (override)
        super().correr() #chamando a classe pai
        print("Papagaio!")

    def falar(self):
        print("falar")

cao = Cao("marrom", "grande", "10", "golden")
cao.correr()
print(cao,"\n") #possível printar dessa forma devido ao método mágico __str__

passaro = Passaro("verde", "pequeno", "300g")
print(passaro,"\n")

papagaio = Papagaio("Verde", "médio", "1kg")
papagaio.correr() #herda de animal
papagaio.voar() #herda de passaro
papagaio.falar() #papagaio
papagaio.latir() #cao
print(papagaio)