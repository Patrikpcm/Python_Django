"""
Quando criamos pacotes (uma pasta contendo conteúdos), essa pasta deve conter o arquivo
__init__.py para que seja reconhecida como um pacote.
Observar o pacote estoque e o subpacote utilidades.
"""

from estoque.produto import cadastrar_produto
produto = {'nome': 'Notebook', 'preco':1200}
cadastrar_produto(produto)


print('')


from estoque.inventario import atualizar_quantidade_produto
produto2 = {'nome':'Notebook', 'quantidade':103}
atualizar_quantidade_produto(produto2)


print('')


lista_produtos =[
    {'nome': 'Notebook', 'preco':8000.0},
    {'nome': 'Xbox', 'preco':5000.99},
    {'nome': 'Celular', 'preco':4001.50}
]

from estoque.utilidades.moeda import formatar_real
for produto in lista_produtos:
    nome = produto['nome']
    preco = formatar_real(produto['preco'])
    print(f'Produto: {nome}, Preço: {preco}')