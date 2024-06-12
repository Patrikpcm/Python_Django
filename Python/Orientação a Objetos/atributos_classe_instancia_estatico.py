"""
Atributos de classe: Vinculado à classe(todo objeto tem e é igual)
Atributos de instância: Vinculados às instâncias dos objetos
"""

class Pessoa:
    planeta = "terra" #planeta é atributo de classe
    def __init__(self, nome) -> None:
        self.nome = nome #nome é atributo de instância

    def exibir_nome(self): #método de instância. Não consigo acessar usando Pessoa.exibir_nome(), por exemplo.
        print(f'Nome: {self.nome}')

    @classmethod
    def exibir_planeta(cls): #decorator classmethod é utilizado para chamar métodos de classe
        print(f'Planeta: {cls.planeta}') #por essa razão utilizamos cls em vez de self.
                                        #cls = classe
                                        #self = instância

    #método estático, não sabe nada da classe ou instância
    @staticmethod
    def recuperar_planetas_habitaveis(): #não passo nem self nem cls. Não consigo nem acessar nome e nem planeta, por exemplo
        print("Terra e Marte")

p1 = Pessoa("João")
p1.planeta = "Marte" #alterando o planeta da pessoa1
#A partir desse momento, p1 tem uma instância própria de planeta. Não é afetada diretamente
#mesmo modificando a classe
print(p1.nome)
print(p1.planeta)
p1.exibir_nome()

p2 = Pessoa("Mario")
print(p2.nome)
print(p2.planeta)

Pessoa.planeta = "Mercúrio" #alterando o planeta de todas as instâncias de Pessoa que não tiveram o planeta alterado diretamente
Pessoa.exibir_planeta() #vê atributos e métodos de classe
print(p1.planeta) #Vai exibir informações da INSTÂNCIA e não da classe, por essa razão o planeta continua sendo Marte
print(p2.planeta)
p1.exibir_planeta() #Vai exibir informações da classe e não da instância. Por isso ambos são mercurio
p2.exibir_planeta() #Vai exibir informações da classe e não da instância. Por isso ambos são mercurio

print("")

Pessoa.recuperar_planetas_habitaveis()
p1.recuperar_planetas_habitaveis()
p2.recuperar_planetas_habitaveis()