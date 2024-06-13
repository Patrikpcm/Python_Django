#converter o ponto decimal em vírgula e adicionar o símbolo de real ao preço

def formatar_real(preco):
    return f'R${preco:.2f}'.replace('.',',')