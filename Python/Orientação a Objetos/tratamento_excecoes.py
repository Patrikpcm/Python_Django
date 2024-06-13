
lista = [0,1,2]

try:#tente
    print(lista[3])
except:#exceto
    print("Índice não existe!\n")

try:#tente
    print(lista[2])
except IndexError as erro: #erro específico para range de lista
    print(f'Erro de índice: {erro}')
except Exception as erro: #exception é um erro genérico
    print(erro)
else:
    print("Executou com sucesso.\n")

print("Continuando execução...")
