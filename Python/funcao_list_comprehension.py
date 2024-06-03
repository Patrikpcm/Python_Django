"""
List Comprehension: É uma construção sintática para a criação
de uma lista baseada em listas existentes. Pode substituir 
filter e reduce
"""

lista = [10, 10, 20, 20, 30, 35, 40, 45]
nova = [item for item in lista] #copiando a lista
print (nova)

nova2 = [item*2 for item in lista] #multiplicando itens por 2
print(nova2)

nova3 = [item>20 for item in lista] #verificando se os itens são maiores que 20
print(nova3)

nova4 = [item for item in lista if item>20] #copiando apenas itens maiores que 20
print(nova4)

nova5 = [item for item in lista if item>20 if item <40] 
print(nova5)#copiando apenas itens maiores que 20 e menores que 40

nova6 = [item if item >=20 and item < 40 else "outRange" for item in lista] 
print(nova6)#substituindo itens menores que 20 e maiores que 40 por "outRange"