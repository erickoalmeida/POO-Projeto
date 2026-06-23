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

    opcao = str(input("Digite uma opção: "))

    if opcao == "1":
        nome = input("Digite o nome do jogador: ")
        jogo.adicionar_jogador(nome)
    elif opcao == "2":
        tipo = input("Tipo de poção ('comum' ou 'arremessavel'): ")
        if tipo in ("comum", "arremessavel"):
            nome = input("Digite o nome da poção: ")
            if nome == None:
                print("Nome de poção inválido.")
            else:
                jogo.adicionar_pocao(nome, tipo)
        else:
            print("Tipo inválido. Use 'comum' ou 'arremessavel'.")
    elif opcao == "3":
        for i in jogo.jogadores:
            if i.ativo:
                print(i.nome)
        nome = input("Digite um nome do jogador que deseja excluir: ")
        jogo.excluir_jogador(nome)
    elif opcao == "4":
        for i in jogo.pocoes:
            if i.ativo:
                print(i.nome)
        pocao_excluir = input("Digite um nome da poção que deseja excluir: ")
        jogo.excluir_pocao(pocao_excluir)
    elif opcao == "5":
        #print(dados.jogadores)
        for i in jogo.jogadores:
            if(i.ativo == True):
                print(i.nome)
    elif opcao == "6":
        for i in jogo.pocoes:
            if(i.ativo == True):
                print(i.nome, i.tipo)
