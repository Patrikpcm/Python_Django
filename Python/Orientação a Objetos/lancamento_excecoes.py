def dividir(n1,n2):
    try:
        print(f'resultado: {n1/n2}')
    except ZeroDivisionError as erro:
        print(f'Erro na função: {erro}')
        raise   #Usado para jogar o erro(lançar a exceção) para cima. Se não usarmos, o exception
                #fora de dividir (Erro do desenvolvedor) não será executado, pois
                #uma exceção já foi lançada.


try:
    dividir(10,0)
except Exception as erro:
    print(f'Erro do desenvolvedor: {erro}')

print("Execução terminada!\n")

###########################################

def dividir2(n1,n2):
    if n2 == 0:
        raise ValueError("Exceção lançada: Não é possível dividir por zero.")
    else:
        print(f'resultado: {n1/n2}')

try:
    dividir2(10,0)
except ValueError as erro:
    print(erro)

print("Execução terminada!\n")

################ EXCEÇÃO PERSONALIZADA ###########################

class OpcaoInvalidaError(Exception):
    pass


def seleciona_opcao(opcao):
    if opcao == '1':
        print("Cartões de crédito")
    elif opcao == '2':
        print("Financiamentos")
    elif opcao == '3':
        print ("Falar com um atendente")
    else:
        raise OpcaoInvalidaError("Opção Inválida")


try:
    seleciona_opcao('4')
except OpcaoInvalidaError as erro:
    print(erro)

print("Execução terminada!\n")