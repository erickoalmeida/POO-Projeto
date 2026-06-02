from models import *

jogo = Jogo()

while True:
    print("=====================\n")
    print("   [POÇÕES/MAKER]   \n")
    print("       .....         ")
    print("     .:=====::       ")
    print("     :-***#*::       ")
    print("      ::: ++         ")
    print("     .::: +++        ")
    print("   .:-=-+###*++      ")
    print("  :-#=-+*###%##++    ")
    print("  :-#=-*#######++    ")
    print("  :=#######*=*#++    ")
    print("  +*##%###**+##++    ")
    print("    +++++++++++      ")
    print("1................ Cadastrar Jogador")
    print("2................ Cadastrar Poção")
    print("3................ Excluir Jogador")
    print("4................ Excluir Poção")
    print("5................ Visu. Jogadores")
    print("6................ Visu. Poções")

    opcao = input("Digite uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do jogador: ")
        if nome == None:
            print("Nome inválido.")
        else:            
            achou = False
            for jogador in jogo.jogadores:
                if jogador.nome == nome:
                    achou = True
            
            if achou == True:
                print("Já existe uma pessoa com esse nome")
            else:
                jogador = Player(nome)
                jogo.jogadores.append(jogador)
                print("Jogador", nome, "cadastrado com sucesso!")
    elif opcao == "2":
        tipo = input("Tipo de poção ('comum' ou 'arremessavel'): ")
        
        """if tipo in ("comum", "arremessavel"):
            nome = input("Digite o nome da poção: ")
            for i in 
                if nome == None:
                    print("Nome de poção inválido.")
                else:
                    pocao = Pocao(nome, tipo)


                    jogo.pocoes.append(pocao)
                    print("Poção:", nome, "do tipo:", tipo, ",cadastrada com sucesso!")"""

    elif opcao == "3":
        nome = input("Digite um nome do jogador que deseja excluir: ")
        for jogador in jogo.jogadores:
            if jogador.nome == nome:
                jogador.ativo = False
                print("Jogador removido com sucesso!")
    elif opcao == "4":
        pocao_excluir = input("Digite um nome da poção que deseja excluir: ")
        for pocao in jogo.pocoes:
            if pocao.nome == pocao_excluir:
                pocao.ativo = False
                print("Poção removida com sucesso!")
    elif opcao == "5":
        for i in jogo.jogadores:
            if i.ativo == True:
                print(i.nome)
    elif opcao == "6":
        for i in jogo.pocoes:
            if i.ativo == True:
                print(i.nome, i.tipo)
                
