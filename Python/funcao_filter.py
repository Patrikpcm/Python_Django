
"""
filter -> filtra dados retornando uma expressão Verdadeiro ou Falso.
ex: lista = [10,20,30,40] ? num > 20
10 - False
20 - False
30 - True
40 - True

Retorna uma nova lista somente com elementos true.
nova_lista = [30,40]
"""

lista = [1,2,3,4,5,10,20,30,35,40]
nova_lista = filter(lambda n: n>20, lista)
print(type(nova_lista)) #retorna um objeto tipo filter
print(list(nova_lista))


