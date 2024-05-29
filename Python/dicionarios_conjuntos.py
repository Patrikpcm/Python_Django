"""
Diferente de listas e tuplas que tem seus elementos atribuídos a um índice automáticamente,
dicionários podem tem esses itens criados junto com os elementos. Por essa razão, dicionários
são conhecidos como estruturas Chave/Valor
"""
#veja o exemplo abaixo, o primeiro item é a chave(índice) e o segundo o valor.
dicionario = {
    "correr":"deslocar-se ou mover-se rapidamente",
    "ligar":"Estabelecer uma comunicação",
    "parar":"Ato de cessar o movimento",
}

print(dicionario)
print(dicionario["correr"])

carro = {
    "modelo":"Fusca",
    "marca":"Volkswagem",
    "ano":1970,
    "donos":["Marcos", "Golias", "Murilo", "Maurice"]
}

carro["donos"].append("Pedro") #Adicionando um elemento na lista do dicionário
print(carro["donos"]) 
print(carro['donos'][0:2])#todas as funções de lista se aplicam...

print ("-------------\n")

carro['km'] = 200.000 #Adicionando mais uma chave/valor para carro
carro['ano'] = 1979 #modificando o valor de uma chave já existente
#também posso atualizar valores utilizando update
carro.update({"ano":1983}) #modificando ano
carro.update({"cor":"verde"}) #criando cor
print(carro)

print("-----------\n")

print(carro.keys()) #imprimindo somente as chaves 
print(carro.values()) #imprimindo só os valores
print(carro.items()) #cria uma lista de tuplas com cada item separado
print(carro.get('ano')) #recuperando um valor com get
"""O interessante de get é que caso o valor de chave solicitado não exista, ele
pode retornar um valor configurado como padrão. Veja os exemplos abaixo"""
print(carro.get('ano', 1960)) #retorna o ano correto: 1983
print(carro.get('rodas', 13)) #retorna a roda aro 13, pois essa informação não existe

print("-----------\n")

del carro['ano'] #removendo o valor do dicionário
valor = carro.pop("cor") #removendo um valor e retornando-o
print(carro)
print('A cor do carro, removido com pop(), é: {}'.format(valor))
carro.clear() #limpando as informações de dicionário
print("\n\n\n")

"""###########################################################################"""
"""
set é um conjunto de itens desordenados e que não permmite repetições
"""
conjunto = {"Patrik","Patrik", "Luiz", "Luiz", "Gogola", "Gogola"}
print(type(conjunto))
print(conjunto)

print("-----------\n")

carros = {"fusca", "gol", "147"}
carros2 = {"golf", "fusca", "voyage"}
uniao = carros.union(carros2) #fazendo união de 2 conjuntos
interseccao = carros.intersection(carros2) #pegando o que é igual nos 2 sets
print (uniao) #fusca se repetia, portando foi removido do novo set
print (interseccao) #fusca se repetia, portanto é o único presente na interseccao

carros.add("fusca") #nada acontece pois fusca já existe
carros.add("ranger")
carros.remove("147") #removendo um item

print(carros)
