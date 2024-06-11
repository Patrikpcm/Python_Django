"""
Pilar 1 da Orientação a Objetos - Abstração
(Exemplos de abstração de um carro quanto a contextos de Autopeças e Uber)
Modelo, Entidade, Identidade
Características e Ações(métodos)
"""

class Autopecas:
    pedido_pecas = []

    def __init__(self, marca='indefinido', carro='indefinido', modelo='indefinido', motor=1.0, ano=1900) -> None:
        #características
        self.marca = marca
        self.carro = carro
        self.modelo = modelo
        self.motor = motor
        self.ano = ano
                
    #ações(métodos)
    def pedidos(self, peca):
        self.pedido_pecas.append(peca)
                    


class Uber:
    def __init__(self, motorista, carro, cor, placa) -> None:
        self.motorista = motorista
        self.carro = carro
        self.cor = cor
        self.placa = placa
        

#identidade = nome; entidade = instância da classe
#ex: carro_ana e carro_ju são identidades diferentes
#mas ambos são instâncias de Autopecas
pecas = Autopecas("Toyota", "Corolla", "Xei", 1.8, 2001)

pecas.pedidos("parachoque")
print(pecas.marca)
print(pecas.pedido_pecas)
