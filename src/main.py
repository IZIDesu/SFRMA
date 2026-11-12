running=True
acoes = [#menu inicial
        ["Sair",
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

        #menu do dataset: A plataforma deve permitir carregar os dados a partir dos ficheiros CSV fornecidos no Moodle: robots.csv, locations.csv e tasks.csv
         #O ficheiro de tarefas poderá conter tarefas iniciais e deverá incluir, no mínimo: identificador, descrição, origem, destino, prioridade e estado.
         ["Sair", 
         "Carregar datasets"],

        #menu da listagem dos robôs
         #• Apresentar, pelo menos, identificador, modelo, bateria, localização e estado.
         #• A listagem deverá ser ordenada pelo identificador do robô.
         ["Sair", 
         "Apresentar informação reduzida",
         "Apresentar toda a informação",],

        #menu da consulta dos robôs
         #• Pesquisar o robô pelo identificador.
         #• Informar o utilizador caso o robô não exista.
         ["Sair",
          "introduza o ID do robô pretende consultar [ex:R001]"],

        #Listar localizacoes
         #• Apresentar código, nome e distância/valor de referência associado.
         #• Ordenar a listagem alfabeticamente pelo nome ou pelo código.
         ["Sair",
          "Listar todos os robôs",
          "Listar robô particular",], 

        #Criar tarefa: A plataforma deve permitir criar uma nova tarefa a realizar por um robô.
         #• Identificador único
         #• Descrição
         #• Localização de origem
         #• Localização de destino
         #• Prioridade (baixa, média ou alta)
         #• Estado (inicialmente pendente)
         #• Robô atribuído (inicialmente vazio, se ainda não tiver sido feita atribuição)
            #regras:
         #• A origem e o destino devem corresponder a localizações existentes.
         #• O identificador da tarefa não pode estar repetido.
         #• A prioridade deve ser validada.
         ["Sair"], 

        #Listar tarefas: A plataforma deve permitir apresentar todas as tarefas existentes
         #• Apresentar identificador, descrição, origem, destino, prioridade, estado e robô atribuído.
         #• Permitir distinguir tarefas pendentes, atribuídas, em execução, concluídas e canceladas.
         ["Sair"], 
        
        #Atribuir tarefa a um robo: A plataforma deve permitir atribuir uma tarefa pendente a um robô.
         #• O robô deve existir e estar disponível.
         #• O robô deve possuir um nível de bateria igual ou superior a 25%.
         #• A tarefa deve encontrar-se no estado pendente.
         #• Após a atribuição, a tarefa passa ao estado atribuída e o robô passa ao estado ocupado.
         ["Sair"], 

        #Executar tarefa: A plataforma deve simular a execução de uma tarefa previamente atribuída a um robô.
         #• A tarefa deve estar atribuída a um robô válido.
         #• A execução deve calcular um consumo de bateria com base numa regra: Exemplo: 𝑐𝑜𝑛𝑠𝑢𝑚𝑜 = 𝑑𝑖𝑠𝑡â𝑛𝑐𝑖𝑎 ∗ 0.2
         #Nota: bateria não pode ficar abaixo de 0%
         #• No final da execução, a localização do robô deve passar a corresponder ao destino da
         #tarefa.
         #• A tarefa deve passar ao estado concluída e o robô deve regressar ao estado disponível.
         ["Sair"], 

        #Carregar bateria de um robo: A plataforma deve permitir simular o carregamento da bateria de um robô.
         #• O robô deve existir.
         #• O carregamento deve atualizar o nível de bateria para 100%.
         #• O estado do robô deve ser atualizado de forma coerente durante e após o carregamento.
         ["Sair"], 

        #Consultar estado da frota: A plataforma deve apresentar um resumo do estado da frota e das tarefas
         #• Apresentar o número total de robôs.
         #• Apresentar quantos robôs se encontram disponíveis, ocupados, em carregamento e indisponíveis.
         #• Calcular e apresentar a bateria média da frota.
         ["Sair"], 

        #Editar tarefa: A plataforma deve permitir alterar uma tarefa existente.
         #• Pesquisar a tarefa pelo seu identificador.
         #• Permitir alterar descrição, origem, destino e prioridade.
         #• Não permitir alterações incoerentes com o estado da tarefa, por exemplo alterar uma tarefa já concluída.
         ["Sair"], 

        #Apagar tarefa: A plataforma deve permitir remover uma tarefa existente.
         #• Pesquisar a tarefa pelo seu identificador.
         #• Apenas tarefas pendentes ou canceladas poderão ser removidas.
         #• Após a remoção, apresentar confirmação ao utilizador.
         ["Sair"], 
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

localizacao_dos_robos = ["Lisboa",
                         "Porto",
                         "Sintra",
                         "Lisboa",
                         "Faro",
                         "Lisboa",
                         "Faro",
                         "Porto",
                         "Lisboa",
                         "Lisboa",
                         "Lisboa",
                         "Lisboa",
                         "Faro",
                         "Lisboa",
                         "Faro",
                         "Porto",]

tabela_tarefas = []


#A função "is_valid_number" que serve para: 
    #validar se a string que é atribuida ao Parâmetro "string" é um numero, com o alcançe 
    # maximo do da lista/array atribuido ao Parâmetro "array" e 
    
    #retorna um boleano ou se quiser que retorne o numero em vez da string coloco o 
    # argumento "return_int" verdadeiro

def is_valid_number(string,array,return_int=False):
    if string.isdigit(): #Verificação se o argumento "string" é um inteiro
        if 0>int(string) or (len(array)-1)<int(string): #verifica se es
            print("Introduza uma ação valida!") #imprime uma mensagem informativa ao utilizador
            return(False) #retorna "False"
        if return_int: #verifica se o argumento "return_int" é True
            return(int(string)) #retorna a string "string" num numero inteiro
        else: #se nenhuma das condições enteriores for verdadeira
            return(True) #retorna "True"
    else: #se a verificação isdigit() for falsa
        print("Introduza um valor valido") #imprime uma mensagem informativa ao utilizador
        return(False) #retorna "False"

#A função "menu" que serve para:
# ilustrar fácilmente o menu com cabeçalho e as opções
# deixa o utilizador introduzir a opção e retorna a mesma

def menu(numero_do_menu=0,input_on=True,no_menu=False):
    if not no_menu: #Verifica se o argumento "no_menu" for "False"
        if numero_do_menu == 0: #Verifica se o argumento "numero_do_menu" é 0
            print(f"=============== ROBOFLEET ===============") #imprime o cabeçalho
        else: #Verifica se o argumento "numero_do_menu" é diferente de 0
            print(f"=============== {acoes[0][numero_do_menu]} ===============") #imprime o cabeçalho da respetiva instrução
        for acao in range(len(acoes[numero_do_menu])): #loop para ilustrar todas as opções do menu
            print(f"{acao}. {acoes[numero_do_menu][acao]}") #ilustra o numero da ação mais a ação em si
    if input_on: #Verifica se o argumento "input_on" é "True"
        resposta = input("Escolha uma opcao:\n") #imprime a mensagem ao utilizador
        return(resposta) #retorna a mensagem que o utilizador introduziu






############################################
###### Pertencem á Lista de funções ########
############################################

#menu do dataset: A plataforma deve permitir carregar os dados a partir dos ficheiros CSV fornecidos no Moodle: robots.csv, locations.csv e tasks.csv
 #O ficheiro de tarefas poderá conter tarefas iniciais e deverá incluir, no mínimo: identificador, descrição, origem, destino, prioridade e estado.
def carregar_datasets(escolha,acao): #1
    None


#menu da listagem dos robôs
 #• Apresentar, pelo menos, identificador, modelo, bateria, localização e estado.
 #• A listagem deverá ser ordenada pelo identificador do robô.
def listar_robos(escolha,acao,repeticao=True): 
    while repeticao: #entra em loop se o argumento/(variavel local) for "True" 
        if escolha == 0: #Verifica se o argumento "escolha" é 0
            repeticao = False #mete a variavel repeticao como falso, parando o loop
        elif escolha == 1: #verifica se o argumento "escolha" é 1
            for robo in lista_dos_robos: #loop que imprime ao utilizador a informação dos robôs
                print(robo) #imprime a informação do robô
        elif escolha == 2: #verifica se o argumento "escolha" é 2
            robo_counter = 0 #criação de uma variavel local, para fazer a contagem dos robôs
            for robo in lista_dos_robos: #loop que imprime ao utilizador a informação dos robôs
                print(f"{robo} em {localizacao_dos_robos[robo_counter]}") #imprime a informação do robôs + localização
                robo_counter += 1 #incrementa 1 ao contador
        else: #verifica apenas se nenhuma das verificações assima não der
            print("Introduza uma ação valida!\n") #imprime informação
        
        if repeticao: #verifica se o argumento "repeticao" é "True"
            escolha = is_valid_number(menu(acao)) #ulustra o menu e pede ao utilizador uma ação

#menu da consulta dos robôs
 #• Pesquisar o robô pelo identificador.
 #• Informar o utilizador caso o robô não exista.
def consultar_robo(escolha,acao,impressao=True,repeticao=True): #3
    while repeticao: #entra em loop se o argumento/(variavel local) for "True" 
        if escolha == 1: #Verifica se o argumento "escolha" é 0
            robo_consultar = menu(no_menu=True) 
            if robo_consultar in lista_dos_robos:
                if impressao:
                    print(f"{robo_consultar}, existe!")
                return(True)
            else:
                if impressao:
                    print(f"{robo_consultar}, não existe!")
                return(False)

        if repeticao:
            escolha = int(menu(acao))

#Listar localizacoes
 #• Apresentar código, nome e distância/valor de referência associado.
 #• Ordenar a listagem alfabeticamente pelo nome ou pelo código.
def listar_localizacoes(escolha,acao, repeticao=True): #4
    while repeticao:
        if escolha == 1:
            for robo in range(lista_dos_robos):
                print(f"{lista_dos_robos[robo]} está em {localizacao_dos_robos[robo]}")
        elif escolha == 2:
            robo_escolha = menu(no_menu=True)
            consultar_robo(robo_escolha)
        
        if repeticao:
            escolha = int(menu(acao))
        
#Criar tarefa: A plataforma deve permitir criar uma nova tarefa a realizar por um robô.
 #• Identificador único
 #• Descrição
 #• Localização de origem
 #• Localização de destino
 #• Prioridade (baixa, média ou alta)
 #• Estado (inicialmente pendente)
 #• Robô atribuído (inicialmente vazio, se ainda não tiver sido feita atribuição)
    #regras:
 #• A origem e o destino devem corresponder a localizações existentes.
 #• O identificador da tarefa não pode estar repetido.
 #• A prioridade deve ser validada.
def criar_tarefa(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))

#Listar tarefas: A plataforma deve permitir apresentar todas as tarefas existentes
 #• Apresentar identificador, descrição, origem, destino, prioridade, estado e robô atribuído.
 #• Permitir distinguir tarefas pendentes, atribuídas, em execução, concluídas e canceladas.
def listar_tarefas(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))
    
#Atribuir tarefa a um robo: A plataforma deve permitir atribuir uma tarefa pendente a um robô.
 #• O robô deve existir e estar disponível.
 #• O robô deve possuir um nível de bateria igual ou superior a 25%.
 #• A tarefa deve encontrar-se no estado pendente.
 #• Após a atribuição, a tarefa passa ao estado atribuída e o robô passa ao estado ocupado.
def atribuir_tarefa_robo(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))

#Executar tarefa: A plataforma deve simular a execução de uma tarefa previamente atribuída a um robô.
 #• A tarefa deve estar atribuída a um robô válido.
 #• A execução deve calcular um consumo de bateria com base numa regra: Exemplo: 𝑐𝑜𝑛𝑠𝑢𝑚𝑜 = 𝑑𝑖𝑠𝑡â𝑛𝑐𝑖𝑎 ∗ 0.2
 #Nota: bateria não pode ficar abaixo de 0%
 #• No final da execução, a localização do robô deve passar a corresponder ao destino da
 #tarefa.
 #• A tarefa deve passar ao estado concluída e o robô deve regressar ao estado disponível.
def executar_tarefa(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))

#Carregar bateria de um robo: A plataforma deve permitir simular o carregamento da bateria de um robô.
 #• O robô deve existir.
 #• O carregamento deve atualizar o nível de bateria para 100%.
 #• O estado do robô deve ser atualizado de forma coerente durante e após o carregamento.
def carregar_bateria_robo(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))
    
#Consultar estado da frota: A plataforma deve apresentar um resumo do estado da frota e das tarefas
 #• Apresentar o número total de robôs.
 #• Apresentar quantos robôs se encontram disponíveis, ocupados, em carregamento e indisponíveis.
 #• Calcular e apresentar a bateria média da frota.
def consultar_estado_frota(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))
    
#Editar tarefa: A plataforma deve permitir alterar uma tarefa existente.
 #• Pesquisar a tarefa pelo seu identificador.
 #• Permitir alterar descrição, origem, destino e prioridade.
 #• Não permitir alterações incoerentes com o estado da tarefa, por exemplo alterar uma tarefa já concluída.
def editar_tarefa(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))
    
#Apagar tarefa: A plataforma deve permitir remover uma tarefa existente.
 #• Pesquisar a tarefa pelo seu identificador.
 #• Apenas tarefas pendentes ou canceladas poderão ser removidas.
 #• Após a remoção, apresentar confirmação ao utilizador.
def apagar_tarefa(escolha,acao, repeticao=True):
    while repeticao:
        if repeticao:
            escolha = int(menu(acao))



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
    acao = is_valid_number(menu(), acoes[0],return_int=True)
    if acao == 0:
        running = False
    else:
        lista_funções[int(acao)-1](is_valid_number(menu(acao), acoes[0], return_int=0),acao)
        
