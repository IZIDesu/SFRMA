Running=True
ações = ["Sair",
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
         "Apagar tarefa"]

while Running:
    print("=============== ROBOFLEET ===============")
    for i in range(len(ações)):
        print(f"{i}. {ações[i]}")
    ação = input("Escolha uma opcao:\n")

    if ação.isdigit():
        if ação == "0":
            print("A sair do programa")
            Running = False

        elif ação == "1":
            print("Datasets Carregados!")

        elif ação == "2":
            print("Listar robos")

        elif ação == "3":
            print("Consultar robo")

        elif ação == "4":
            print("Listar localizacoes")

        elif ação == "5":
            print("Criar tarefa")

        elif ação == "6":
            print("Listar tarefas")

        elif ação == "7":   
            print("Atribuir tarefa a um robo")

        elif ação == "8":
            print("Executar tarefa")

        elif ação == "9":
            print("Carregar bateria de um robo")

        elif ação == "10":
            print("Consultar estado da frota")

        elif ação == "11":
            print("Editar tarefa")

        elif ação == "12":
            print("Apagar tarefa")

        else:
            print("Introduza uma ação valida!")
    else:
        print("Introduza um valor valido")