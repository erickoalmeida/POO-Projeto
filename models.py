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

    def excluir_jogador(self, nome):
        if nome is None:
            print("Nome inválido.")
            return

        for jogador in self.jogadores:
            if jogador.nome == nome:
                self.jogadores.remove(jogador)
                print("Jogador removido com sucesso!!")
                return

        print("Jogador não encontrado.")

    def excluir_pocao(self, nome):
        if nome is None:
            print("Nome de poção inválido.")
            return

        for pocao in self.pocoes:
            if pocao.nome == nome:
                self.pocoes.remove(pocao)
                print("Poção removida com sucesso!!")
                return

        print("Poção não encontrada.")
