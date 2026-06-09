class Player:
    def __init__(self, nome):
        self.nome = nome

class Pocao:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Jogo:
    def __init__(self):
        self.jogadores = []
        self.pocoes = []