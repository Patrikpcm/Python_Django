"""
ENCAPSULAMENTO
O Encapsulamento serve para esconder detalhes da implementação, dando mais segurança
a sua aplicação. O Encapsulamento serve para controlar o acesso aos atributos e métodos
de uma classe.
"""

class Filtro:
    def __init__(self, imagem) -> None:
        self.imagem = imagem
    #digamos que isso seria uma classe que outra pessoa criou...
    def preto_e_branco(self): 
        print(f'{self.imagem} com filtro preto e branco')

    #...essa também. Usamos sem saber os detalhes de como funciona,
    #apenas aplicando os efeitos desejados na suposta imagem. (encapsulamento)
    def foto_envelhecida(self): 
        print(f'{self.imagem} com filtro foto envelhecida')


filtro = Filtro("foto_cachorro")
filtro.preto_e_branco()
print("")

"""Utilizando controladores de acesso: Getters e Setters"""
class Conta:
    def __init__(self, saldo) -> None:
        self._numero = 0
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    @property #decorator para modificar os métodos
    def numero(self):
        return self._numero
    
    @numero.setter #decorator para modificar os métodos
    def numero(self, numero):
        if numero > 0:
            self._numero = numero
        else:
            print("Número inválido")

conta = Conta(800)
#conta.set_numero(318288)
conta.sacar(100)
conta.depositar(200)
#conta._saldo = 0 #Método errado de alterar valor do saldo. Por isso usamos Get e Setters
print(conta._saldo)
#conta.set_numero(232323)
#print(conta.get_numero())
conta.numero = 311111
print(conta.numero)