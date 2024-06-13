"""
Um módulo é um arquivo contendo definições e instruções Python que podem
ser importadas para utilização de seus recursos.
"""

"""
def somar(n1,n2):
    return (n1+n2)


def subtrair(n1,n2):
    return (n1-n2)


def multiplicar(n1,n2):
    return (n1*n2)


def dividir(n1,n2):
    return (n1/n2)
"""
###############################3

#import operacoes
#print(operacoes.somar(1,4))

#from operacoes import somar, subtrair
#print(somar(1,4))

from operacoes import * #importar tudo
print(dividir(1,4))

print(__name__)#mostra qual módulo esta sendo executado no momento
#Obs: Módulo principal MAIN é o que esta sendo executado no momento, diretamente pelo
#desenvolvedor.

#import pymysql