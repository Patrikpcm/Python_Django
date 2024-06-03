"""
Funções como objeto de primeira classe, são funções que se comportam
como qualquer tipo nativo de uma determinada linguagem
"""

def somar(a,b):
    return a+b


def subtrair(a,b):
    return a-b


lista = [somar, subtrair] #passando as funções como objetos de uma lista

for funcao in lista:
    print(funcao(1,2)) #primeiro executa 1+2, depois 1-2
                       #Esse é o tipo de coisas que não se pode executar em outras linguagens


a = somar #atribuir a função a uma variável
b = "Patrik"
print(a(1,2),'\n')


"""Funções de ordem superior são funções que recebem funções como parâmetros
e/ou retornam funções como resposta
"""
carrinho_compras = [
    {'produto':'fone de ouvido', 'preco':500},
    {'produto':'controle xbox', 'preco':400},
    {'produto':'celular', 'preco':2400},
]

print(carrinho_compras)

def calcular_desconto(lista, funcao):
    for produto in lista:
        #print(produto['preco'])
        item_desconto = funcao(produto['preco'],10) #utilizando a funcao passada como atributo para realizar o calculo de desconto
        print(item_desconto)

calcular_desconto(carrinho_compras,somar) #passando uma função como parâmetro da função
print("\n")
calcular_desconto(carrinho_compras,subtrair) #passando uma função como parâmetro da função