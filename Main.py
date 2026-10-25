escolha = input('''
=============== ROBOFLEET ==========
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
''')

if escolha == "0":
    print("A sair do programa")
    exit()
if escolha == "1":
    print("Carregar datasets")
elif escolha == "2":
    print("Listar robos")
elif escolha == "3":
    print("Consultar robo")
elif escolha == "4":
    print("Listar localizacoes")
elif escolha == "5":
    print("Criar tarefa")
elif escolha == "6":
    print("Listar tarefas")
elif escolha == "7":   
    print("Atribuir tarefa a um robo")
elif escolha == "8":
    print("Executar tarefa")
elif escolha == "9":
    print("Carregar bateria de um robo")
elif escolha == "10":
    print("Consultar estado da frota")
elif escolha == "11":
    print("Editar tarefa")
elif escolha == "12":
    print("Apagar tarefa")
else:
    print("Introduza uma ação valida!")
