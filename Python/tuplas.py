#Tuplas são como listas, porem são IMUTÁVEIS

#tupla = (10 ) criando tupla sem vírgula, o tipo será <int>
tupla = (10,) #adicionando vírgula, passa a ser considerado uma tupla
print(type(tupla))
print(tupla)

tupla2 = ("Patrik", "Luiz", "Gogola", 50, 10) #adicionando tipos diferentes
#tupla2[0] = "alterado" #isso gera erro pois a tupla é imutável
print(tupla2)
print(tupla2[2])
print(tupla2[-1]) #de trás pra frente
print(tupla2[:3]) #imprimindo até o 3
print("A quantidade de itens nessa tupla é", len(tupla2)) #tamanho da tupla
print("Existe(m)",tupla2.count("Patrik"), "vez(es) o elemento Patrik na tupla") #contando quantidade de itens Patrik
print("O elemento Patrik esta no índice", tupla2.index("Patrik")) #indice do elemento