"""
Relação de Composição: A classe principal(todo) cria uma instância da outra
classe(parte), que se torna parte dela. Quando a classe principal for destruída,
sua instância da outra classe também será.
Ex.: Trem e Vagões. Você pode criar um Trem e esse por sua vez funcionará. Mas
só sera possível adicionar e fazer vagões se moverem se esses forem adicionados
a um trem. Quando se exclui um trem, os vagões automaticamente devem ser excluídos
também.
"""

class Usuario:#todo
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, cep, cidade, rua):
        endereco = Endereco(cep,cidade,rua)
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __del__(self):
        print (f"{self.nome} = APAGADO")


class Endereco:#parte
    def __init__(self, cep, cidade, rua):
        self.cep = cep
        self.cidade = cidade
        self.rua = rua

    def __str__(self) -> str:
        return f'CEP: {self.cep}, Cidade: {self.cidade}, Rua: {self.rua}'
    
    def __del__(self):
        print (f"{self.rua} = APAGADO")
    
usuario = Usuario("Patrik")
usuario.inserir_endereco("83535-111", "Campo Longo", "Beatriz Munhoz da Pedra")
usuario.inserir_endereco("11111-111", "California", "California Dreams")
usuario.inserir_endereco("22222-111", "Piraquara", "Rua do presídio")
usuario.listar_enderecos()

del(usuario) #apagando usuario, as ruas automáticamente serão apagadas