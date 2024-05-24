"""
OPERADORES CONDICIONAIS
if      (se)
else    (senão)
"""

idade = 20
condicao = idade >=18 #posso criar uma condição
print(condicao)

idade = 17
condicao = idade >=18
print(condicao)

if(condicao): #Dois pontos indica o começo de um bloco de código, junto com os espaçamentos
    print("Maior de idade")
else:
    print("Menor de idade")


if idade <= 13:
    print ("Criança")
elif idade >=18: # "elif" == "else if"
    print("Adulto")
else:
    print("Adolescente")


"""
OPERADORES TERNÁRIO - condicao ? verdadeiro : falso
"""
print("--------------------------------------\n")
idade = 50
resultado = ('Menor idade','Maior idade')[idade>=18]
"""
Se a condição for verdadeira, ele exibe ou executa o código mais próximo da condição,
ou mais a direita. 
Se for falsa, ele executa o código mais distante da condição.
"""
print(resultado)

resultado = 'Maior de idade' if idade>=18 else "Menor idade"
