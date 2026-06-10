class Player:
    def __init__(self, nome):
        self.nome = nome
        self.ativo = True

class Pocao:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.ativo = True

class Jogo:
    def __init__(self):
        self.jogadores = []
        self.pocoes = []
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
    def adicionar_pocao(self, pocao):
        self.pocoes.append(pocao)
