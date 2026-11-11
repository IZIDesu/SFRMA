running=True
acoes = [["Sair", #menu inicial
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

         ["Sair", #menu do dataset
         "Carregar datasets"],
         
         ["Sair", #menu da listagem dos robôs
         "Apresentar informação reduzida",
         "Apresentar toda a informação",],
         
         ["Sair"], #menu da consulta dos robôs

         ["Sair"], #Listar localizacoes

         ["Sair"], #Criar tarefa

         ["Sair"], #Listar tarefas

         ["Sair"], #Atribuir tarefa a um robo

         ["Sair"], #Executar tarefa

         ["Sair"], #Carregar bateria de um robo

         ["Sair"], #Consultar estado da frota

         ["Sair"], #Editar tarefa

         ["Sair"], #Apagar tarefa
         ]


##Lista provisória
lista_dos_robos = {"R001":["LIMO","100"],
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



def is_valid_number(string,array,return_int=False):
    if string.isdigit():
        if 0>int(string) or (len(array)-1)<int(string):
            print("Introduza uma ação valida!")
            return(False)
        if return_int:
            return(int(string))
        else:
            return(True)
    else:
        print("Introduza um valor valido")
        return(False)


def menu(numero_do_menu=0,input_on=True):
    if numero_do_menu == 0:
        print(f"=============== ROBOFLEET ===============")
    else:
        print(f"=============== {acoes[0][numero_do_menu]} ===============")
    for acao in range(len(acoes[numero_do_menu])):
        print(f"{acao}. {acoes[numero_do_menu][acao]}")
    if input_on:
        resposta = input("Escolha uma opcao:\n")
        return(resposta)


def carregar_datasets():
    None

def listar_robos(escolha):
    for robo in lista_dos_robos:
        print(robo)


def consultar_robo(escolha):
    None

def listar_localizacoes():
    None

def criar_tarefa():
    None

def listar_tarefas():
    None

def atribuir_tarefa_robo():
    None

def executar_tarefa():
    None

def carregar_bateria_robo():
    None

def consultar_estado_frota():
    None

def editar_tarefa():
    None

def apagar_tarefa():
    None




#Lista das funções gerais
lista_funções = [carregar_datasets, 
                 listar_robos, 
                 consultar_robo, 
                 listar_localizacoes, 
                 criar_tarefa, 
                 listar_tarefas, 
                 atribuir_tarefa_robo, 
                 executar_tarefa, 
                 carregar_bateria_robo, 
                 consultar_estado_frota, 
                 editar_tarefa, 
                 apagar_tarefa]


while running:
    acao = menu()
    if is_valid_number(acao, acoes[0]):
        menu(int(acao))
    
        
