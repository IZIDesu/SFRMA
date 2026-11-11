running=True
acoes = [["Sair", #Menu inicial
         "Carregar datasets",
         "Listar robos",
         "Consultar robo",
         "Listar localizacoes",
         "Criar tarefa",
         "Listar tarefas",
         "Atribuir tarefa a um robo",
         "Executar tarefa",
         "Carregar bateria de um robo", 
         "Consultar estado da frota", 
         "Editar tarefa", 
         "Apagar tarefa"],

        ["Sair", #Menu do dataset
        "Carregar datasets"],
         
         ["Sair", #Menu da listagem dos robôs
         "Apresentar informação reduzida",
         "Apresentar toda a informação",],
         
         ["Sair"], #Menu da consulta dos robôs

         [],
         ]

##Lista provisória
Lista_dos_robos = {"R001":["LIMO","100"],
                   "R002":["LIMO","100"],
                   "R003":["LIMO","100"],
                   "R004":["LIMO","100"],
                   "R005":["LIMO","100"],
                   "R006":["TurtleBot","100"],
                   "R007":["TurtleBot","100"],
                   "R008":["TurtleBot","100"],
                   "R009":["TurtleBot","100"],
                   "R010":["TurtleBot","100"],
                   "R0011":["Pioneer","100"],
                   "R0012":["Pioneer","100"],
                   "R0013":["Pioneer","100"],
                   "R0014":["Pioneer","100"],
                   "R0015":["Pioneer","100"],}





def Menu(numero_do_menu=0):
    print("=============== ROBOFLEET ===============")
    for i in range(len(acoes[numero_do_menu])):
        print(f"{i}. {acoes[numero_do_menu][i]}")


def Opcoes(opcao_running=True):
    while opcao_running:
        print("Entrado")
        escolha = input("Escolha uma opcao:\n")


def Datasets():
    None



while running:
    Menu()
    acao = input("Escolha uma opcao:\n")
    if acao.isdigit():
        acao = int(acao)

        if 0>acao or 12<acao:
            print("Introduza uma acao valida!")

        Menu(acao)
        Opcoes()

    else:
        print("Introduza um valor valido")





        #if acao == "0":
        #    print("A sair do programa")
        #    running = False
#
        #elif acao == "1":
        #    print("Datasets Carregados!")
#
        #elif acao == "2":
        #    print("Listar robos")
#
        #elif acao == "3":
        #    print("Consultar robo")
#
        #elif acao == "4":
        #    print("Listar localizacoes")
#
        #elif acao == "5":
        #    print("Criar tarefa")
#
        #elif acao == "6":
        #    print("Listar tarefas")
#
        #elif acao == "7":   
        #    print("Atribuir tarefa a um robo")
#
        #elif acao == "8":
        #    print("Executar tarefa")
#
        #elif acao == "9":
        #    print("Carregar bateria de um robo")
#
        #elif acao == "10":
        #    print("Consultar estado da frota")
#
        #elif acao == "11":
        #    print("Editar tarefa")
#
        #elif acao == "12":
        #    print("Apagar tarefa")

        
