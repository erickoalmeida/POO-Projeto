'''
Heranca
Quando eu quiser aproveitar atributos ou metodos entre classes 
eu uso o conceito de Heranca
 "Um player tem coisas ('ativo', 'nome') ent, ele pode ter coisas de 
 Pocao"
'''
class Players:
    def __init__(self, nome):
        self.nome = nome
        self.ativo = True

class PocoesIlegais:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.ativo = True

class Player(Players):
    def __init__(self, nome):
        super().__init__(nome)

class Pocao(PocoesIlegais):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)

class Jogo:
    def __init__(self):
        self.jogadores = []
        self.pocoes = []
