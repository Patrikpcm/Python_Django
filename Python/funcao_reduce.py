"""
reduce (reduzir): Acumula e reduz uma lista em um único valor.
"""
from functools import reduce #Reduce não vem dentro do builtins do python, portanto deve ser importada

lista_num = [10,10,10]

"""FORMA TRADICIONAL"""
acumula = 0
for item in lista_num:
    acumula += item
print (acumula)


"""USANDO REDUCE"""
funcao = lambda acumulador, item: acumulador+item
#reduce recebe 3 parâmetros: uma função, uma lista e o valor inicial do acumulador
#resultado = reduce(lambda acumulador, item: acumulador+item, lista_num, 0) 
resultado = reduce(funcao, lista_num, 0)
print (resultado)