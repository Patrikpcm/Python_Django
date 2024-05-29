"""mutiplos parâmetros (PACKING)"""
def somarPadrao(n1,n2,n3):
    total = n1 + n2 + n3
    print(f"Total: {total}")

#mas e se eu quisesse passar mais números e não soubesse a quantidade?
#para isso eu uso o PACKING
def somar(*numeros):
    #print(type(numeros)) #o retorno é uma tupla
    total = 0
    for valor in numeros:
        total += valor
    print(f"Total: {total}")

somarPadrao(1,1,1)

somar(1,2,3,4)
somar(1,2)
somar(1)
somar(10,2,3,4,5,6,7,8)


"""multiplos parâmetros (UNPACKING)"""
#no unpacking eu sigo o caminho contrário, pegando 1 objeto e convertendo em vários
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(f"Media: {media}")

#mas eu sei que sempre serão 3 notas, em vez de eu passar cada parâmetro,
#posso passar a lista diretamente e a função faz o unpacking automaticamente
#para isso basta utilizar o * 
notas = [2,3,4]
calcularMedia(*notas) #passando as notas diretamente, sem definir os parâmetros. (unpacking)


"""Parâmetros opcionais & nomeados"""
#quando inicializo o valor, ele passa a ser opcional
def calcularMedia2(nota1, nota2, ponto_extra=0, nota_extra=0): 
    media = (nota1 + nota2) / 2 + ponto_extra
    print(f"Media 2: {media}, Nota Extra: {nota_extra}")

calcularMedia2(9,8)
calcularMedia2(9,8,1) #passando o parâmetro pela ordem, nesse caso, estou dando 1 ponto_extra
calcularMedia2(9,8,nota_extra=2) #posso apontar qual parâmetro desejo usar, nomeando-o na chamda da funlção

