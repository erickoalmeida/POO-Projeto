class Player:
    def __init__(self, nome):
        self.nome = nome
        self.ativo = True

class Jogador_Pro(Player):    
    def __init__(self, nome, data_ficou_pro, apelido):
        super().__init__(nome)
        self.ativo = True
        self.data_ficou_pro = data_ficou_pro   
        self.apelido = apelido

class Jogador_Noob(Player):
    def __init__(self, nome, apelido):
        super().__init__(nome)
        self.ativo = True
        self.apelido = apelido


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
        tipo_player = input("Digite o tipo de jogador ('pro' ou 'noob'): ")
        if tipo_player == "pro" or tipo_player == "Pro":
            data_ficou_pro = input("Digite a data em que o jogador ficou pro (dd/mm/aaaa): ")
            apelido = input("Digite o apelido do jogador: ")
            jogador = Jogador_Pro(nome, data_ficou_pro, apelido)
            self.jogadores.append(jogador)
            print("Jogador", nome, "cadastrado com sucesso!")
        elif tipo_player == "noob" or tipo_player == "Noob":
            apelido = input("Digite o apelido do jogador: ")
            jogador = Jogador_Noob(nome, apelido)
            self.jogadores.append(jogador)
            print("Jogador", nome, "cadastrado com sucesso!")
        else:
            print("Tipo de jogador inválido. Use 'pro' ou 'noob'.")
            return

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
        
