"""
Listas em Python são como arrays em Javascript,
mutável e dinâmica, heterogênea e indexada
"""

lista = ["Patrik", "Pedro", "Luiz", "Emerson", "Caio", "Sabrina", "Josane"]
print(type(lista))
print(dir(lista))

print(lista[0])
print(lista[-1]) # De trás pra frente
print(lista[:3]) #até o índice 2
print(lista[::3]) #imprimindo a cada 3

"""Modificações"""
print("---------------")

lista[0] = "Alterado" #alterando o primeiro índice
lista.append("Novo") #adicionando um elemento no final da lista
print(lista)

del lista[1] #removendo elemento pelo índice (Patrik)
lista.remove("Luiz") #removendo elemento pelo valor
print(lista)

#del lista[:5] #removendo até o 4° elemento
#lista.clear() #limpando a lista
print(lista)

print (len(lista)) #obtendo a quantidade de itens da lista
lista.append("Novo") #adicionando mais um elemento "Novo"
print (lista.count("Novo")) #contando quantos elementos "Novo" possuí a lista
print(lista.index("Novo")) #imprimindo o índice da primeira ocorrência de "Novo" na lista

lista.reverse() #invertendo a ordem da lista
print(lista)

lista.sort()#ordenando a lista
print(lista) 

print("Novo" in lista) #verificando se um elemento esta na lista
print("Novo" not in lista) #verificando se um elemento NÃO esta na lista
print("Joarez" in lista)