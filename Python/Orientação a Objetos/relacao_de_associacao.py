"""
Relação de Associação: É uma das relações mais comuns entre dois objetos,
acontece quando um objeto "utiliza" outro, porém, sem que eles dependam
um do outro.
Ex. Trem e Trilho. O Trem utiliza o trilho, porém esse não faz parte do trem e
vice-versa.
"""

teste = ""  #string vazia (undefined)
teste2 = None  #None == NULL
del teste2
del teste
##################################################################

class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.video_game = None

    def andar(self):
        print(f"Jogador {self.nome} esta andando.")


class VideoGame:
    def __init__(self, nome) -> None:
        self.nome = nome

    def rodar_jogo(self):
        print(f"Rodar jogo no {self.nome}")

jogador = Pessoa("Patrik")
jogador.andar()

videogame = VideoGame("Xbox")

jogador.video_game = videogame #associação de objetos(classes)
jogador.video_game.rodar_jogo() #acessando um método através da associação

