def somar(a,b):
    return a+b


def subtrair(a,b):
    return a-b

variavel = subtrair

print (variavel(1,3))
#######################
lista = [
    {'produto':'fone de ouvido', 'preco':500},
    {'produto':'controle xbox', 'preco':400},
    {'produto':'celular', 'preco':2400},
]

def calcular_desconto(lista, funcao):
    for produto in lista:
        #print(produto['preco'])
        item_desconto = funcao(produto['preco'],10) #utilizando a funcao passada como atributo para realizar o calculo de desconto
        print(item_desconto)



#######################
"""
Uma expressão lambda é uma função anônima, uma maneira de criar uma função
só que essa função não possuí um nome.
"""
#utilizando função lambda (anônima) economizo um return e não possui nome
#passo ela diretamente para uma variável
sub = lambda a,b : a-b 
print (sub(1,3))

sub2 = lambda a,b : print(a-b)
sub2(2,3)
print("\n")
calcular_desconto(lista, lambda a,b : a-b) #passando lambda diretamente como parâmetro da função