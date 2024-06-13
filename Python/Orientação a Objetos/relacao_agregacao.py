"""
Relação de Agregação: Uma classe precisa de outra para executar sua ação, ou seja,
uma classe utiliza outra como parte de si.
Ex.: Farol e Carro. Para o carro acender o farol, ele precisa que o farol esteja ligado
a ele. Entretanto, o carro funciona normalmente sem o mesmo.
"""

class CarrinhoCompras:
    def __init__(self) -> None:
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if(len(self.produtos) > 0):
            for produto in self.produtos:
                print(f"{produto.nome} - R${produto.preco}") #acessando atributos de produto dentro da classe Carrinho
                                                            #relação de agregação
        else:
            print("Carrinho vazio!")

class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def cadastrar_produto(self):
        pass

    def remover_produto(self):
        pass


carrinho = CarrinhoCompras()
    
produto1 = Produto("Notebook", 3000.50)
produto2 = Produto("Celular", 8000.99)

carrinho.listar_produtos()

carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.listar_produtos()