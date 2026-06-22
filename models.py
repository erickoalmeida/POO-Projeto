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

    def adicionar_jogador(self, nome):
        if not nome:
            print("Nome inválido.")
            return

        for jogador in self.jogadores:
            if jogador.nome == nome:
                print("Já existe uma pessoa com esse nome")
                return

        jogador = Player(nome)
        self.jogadores.append(jogador)
        print("Jogador", nome, "cadastrado com sucesso!")
            
    def adicionar_pocao(self, nome, tipo):
        for pocao in self.pocoes:
            if pocao.nome == nome:
                print("Já existe uma pocao com esse nome")
                return
        pocao = Pocao(nome, tipo)
        self.pocoes.append(pocao)
        print("Poção:", nome, "do tipo:", tipo, ",cadastrada com sucesso!")
        
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
                print("pocao removida com sucesso!")
                return
        print("Poção não encontrada.")
        
