"""
map -> mapeia os dados, percorre e altera-os.
map é diferente da função map do c++, a qual é mais parecida com um dicionário python
"""

lista_numeros = [10, 20, 30]

nova_lista = map(lambda n: n*2, lista_numeros) #o retorno da função é um objeto map e não lista

print(lista_numeros)
print(nova_lista) #imprimindo um map
print(list(nova_lista)) #imprimindo a lista
l = list(nova_lista) #transformando o map em lista para uma variável
print(l) 
