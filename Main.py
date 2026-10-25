escolha = int(input('''
======= ======== ROBOFLEET ==========
1. Carregar datasets
2. Listar robos
3. Consultar robo
4. Listar localizacoes
5. Criar tarefa
6. Listar tarefas
7. Atribuir tarefa a um robo
8. Executar tarefa
9. Carregar bateria de um robo
10. Consultar estado da frota
11. Editar tarefa
12. Apagar tarefa
0. Sair
Escolha uma opcao:
'''))

match escolha:
    case 0:
        print("")
        print("A sair do programa")
        exit()
    case 1:
        print("Carregar datasets")
    case 2:
        print("Listar robos")
    case 3:
        print("Consultar robo")
    case 4:
        print("Listar localizacoes")
    case 5:
        print("Criar tarefa")
    case 6:
        print("Listar tarefas")
    case 7:
        print("Atribuir tarefa a um robo")
    case 8:
        print("Executar tarefa")
    case 9:
        print("Carregar bateria de um robo")
    case 10:
        print("Consultar estado da frota")
    case 11:
        print("Editar tarefa")
    case 12:
        print("Apagar tarefa")
    