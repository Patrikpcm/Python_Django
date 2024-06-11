class Animal: #superclasse ou classe pai
    def __init__(self) -> None:
        self.cor = ""
        self.tamanho = ""
        self.peso = ""

    def correr(self):
        print("correr")

    def dormir(self):
        print("dormir")


class Cao(Animal): #subclasse ou classe filha
    def latir(self):
        print("latir")


class Passaro(Animal):#subclasse ou classe filha
    def voar(self):
        print("voar")


cao = Cao()
cao.cor = "marrom"
cao.correr()
print(cao.cor)

passaro = Passaro()
passaro.cor = "verde"
passaro.voar()