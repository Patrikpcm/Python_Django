"""
builtins = recursos integrados
print() é um exemplo de builtin
"""

print("Patrik")
print(type("Patrik")) #imprime o tipo de dado
print(dir()) #mostra os recursos disponíveis do python
__builtins__.print("teste")


"""
Conversão de tipos str, int, float, list
"""

print(1+int('2')) #Somar int e uma string, converte-se a string com int()
print(1+float('2.5'))
print('1'+'2.5')
numero = 9
print(str(numero) + '50')


"""
Conversão automática
"""
print(10/2) #Dois ints retornam um float
print(type(10/2)) #prova real
print(2 + True) #Ele soma por entender que true equivale a 1