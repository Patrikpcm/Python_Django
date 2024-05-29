carro = "Fusca"
preco = 1200

#abordagem moderna
print('carro: '+ carro +', preco: ' + str(preco))
print(f'carro: {carro}, preço: {preco}')

print("\n---------------\n")

#abordagens antigas
print('carro: %s. preco: %.2f' %(carro, preco))
print('carro: {0}, preço: {1}'.format(carro,preco)) #os números servem para definir a posição das variaveis na lista. Mas não são obrigatórios