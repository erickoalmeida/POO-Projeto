from models import *

jogo = Jogo()

while True:
    print("=====================\n")
    print("   [PORÇÕES/MAKER]   \n")
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
    print("\n=====================\n")
    print("1................ Cadastrar Jogador")
    print("2................ Cadastrar Poção")
    print("3................ Excluir Jogador")
    print("4................ Excluir Poção")
    print("5................ Visu. Jogadores")
    print("6................ Visu. Poções")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do jogador: ")
        if nome == "":
            print("Nome inválido.")
        else:
            jogo.jogadores.append(Player(nome))
            print("Jogador", nome, "cadastrado com sucesso!")
    elif opcao == "2":
        tipo = input("Tipo de poção ('comum' ou 'arremessavel'): ")
        if tipo in ("comum", "arremessavel"):
            nome = input("Digite o nome da poção: ")
            if nome == "":
                print("Nome de poção inválido.")
            else:
                jogo.pocoes.append(Pocao(nome, tipo))
                print("Poção:", nome, "do tipo:", tipo, ",cadastrada com sucesso!")
        else:
            print("Tipo inválido. Use 'comum' ou 'arremessavel'.")
    elif opcao == "3":
        nome = input("Digite o nome do jogador a ser excluído: ")
        posicao = 0
        for jogador in jogo.jogadores:
            for jogador in jogo.jogadores:
                if jogador.nome == nome:
                    jogo.jogadores.pop(posicao)
                    print("Jogador", nome, "excluído com sucesso!")
                else:
                    posicao += 1
    elif opcao == "4":
        pocao_excluir = input("Digite o nome da poção a ser excluída: ")
        for pocao in jogo.pocoes:
            posicao = 0
            for pocao in jogo.pocoes:
                if pocao.nome == pocao_excluir:
                    jogo.pocoes.pop(posicao)
                    print("Poção", pocao_excluir, "excluída com sucesso!")
                else:
                    posicao += 1

    elif opcao == "5":
        #print(dados.jogadores)
        for i in jogo.jogadores:
            print(i.nome)
    elif opcao == "6":
        for i in jogo.pocoes:
            print(i.nome, i.tipo)
