import random
import os
import copy

def imprimir_tabela(matrix, tipo_ambiente, quantidade_salas):
    print()
    if tipo_ambiente == 1:
        for row in range(len(matrix)):
            i = 0
            if row != 2:
                while i < quantidade_salas:
                    print(matrix[row][i], end='\t') # Escreve o valor como não descoberto
                    i = i + 1
                print()  # Pule para a próxima linha após cada linha da matriz
        
        print() # Linha do Debug
        i = 0
        while i < quantidade_salas:
            print(Debug[i], end='\t') # Escreve o valor como não descoberto
            i = i + 1

    if tipo_ambiente == 2:
        for row in range(len(matrix)):
            i = 0
            if row != 3:
                while i < quantidade_salas:
                    print(matrix[row][i], end='\t') # Escreve o valor como não descoberto
                    i = i + 1
                print()  # Pule para a próxima linha após cada linha da matriz
        
        print() # Linha do Debug
        i = 0
        while i < quantidade_salas:
            print(Debug[i], end='\t') # Escreve o valor como não descoberto
            i = i + 1

    print("\n\n")

    


def RandomizarPosicaoRobo(AspiradorDePo, quantidade_salas):
    # Verifica se o Robô está na lista já e apaga pra ser trocado
    for i in range(0, quantidade_salas):
        if AspiradorDePo[1][i] == 'Robo':
            AspiradorDePo = ''
    
    # Gera um número aleatório entre 0 - 9
    random_integer = random.randint(0, quantidade_salas - 1)

    # Marca o robô como Robô no array de posicao do robo com base no
    # número aleatório
    AspiradorDePo[1][random_integer] = 'Robo'



def preencher_sala(quantidade_salas, quantidade_salas_sujas, ambiente):
    # Verifica se a quantidade de salas sujas é maior que que a quantidade de salas
    if(quantidade_salas < quantidade_salas_sujas):
        print("Quantidade maior de sujeiras do que salas")
        return 0
    
    while quantidade_salas_sujas != 0:
        random_integer = random.randint(0, quantidade_salas - 1)
        if(ambiente[2][random_integer] == ''):
            ambiente[2][random_integer] = 'Sujo'
            quantidade_salas_sujas = quantidade_salas_sujas - 1
        else:
            continue
    
    for i in range(0, quantidade_salas):
        if(ambiente[2][i] == ''): 
            ambiente[2][i] = 'Limpo'    
    
    return ambiente



def encontrar_posicao_robo(ambiente):
    for i, robo in enumerate(ambiente[1]):
        if robo == 'Robo':
            return i
    return None

def limpar(pos, ambiente):

    ambiente[3][pos] = 'Limpo'
    if ambiente[2][pos] == 'Sujo':
        ambiente[2][pos] = 'Limpo'
        return True
    else:
        return False

def gerar_sujeira(pos, ambiente):
    sujeiraNova = False
    
    random_integer = random.randint(1, 10)
    if random_integer == 5:
        print("\n\n =========== Sujeira Nova ============\n\n")
        while :
            sujeiraNova_posicao = random.randint(0, quantidade_salas - 1)
        
        ambiente[2][sujeiraNova_posicao] = 'Sujo'
        sujeiraNova = True  

def mover(input, ambiente):
    pos = encontrar_posicao_robo(ambiente)

    if input == 'd' and pos + 1 <= quantidade_salas - 1:
        ambiente[1][pos] = ''
        ambiente[1][pos + 1] = 'Robo'
        return limpar(pos+1, ambiente)
        
    elif input == 'a' and pos - 1 >= 0:
        ambiente[1][pos] = ''
        ambiente[1][pos - 1] = 'Robo'
        return limpar(pos-1, ambiente)
    

def mover_manual(input, ambiente, salas_sujas):
    pos = encontrar_posicao_robo(ambiente)

    if input == 'd' and pos + 1 <= quantidade_salas - 1:
        ambiente[1][pos] = ''
        ambiente[1][pos + 1] = 'Robo'

    elif input == 'a' and pos - 1 >= 0:
        ambiente[1][pos] = ''
        ambiente[1][pos - 1] = 'Robo'

    elif input == 'limpar':
        Sala_foi_limpa = limpar(pos, ambiente)
        
        if Sala_foi_limpa == True:
            salas_sujas = salas_sujas - 1

    return salas_sujas
    

def automatico_onisciente(ambiente, quantidade_salas):
    PosicaoRobo = encontrar_posicao_robo(ambiente)
    limpar(PosicaoRobo, ambiente)
    SujeiraEsquerdaMaisLonge_distancia = 0
    SujeiraDireitaMaisLonge_distancia = 0
    SujeiraEsquerdaMaisLonge_posicao = PosicaoRobo
    SujeiraDireitaMaisLonge_posicao = PosicaoRobo
    

    i = PosicaoRobo
    while i < quantidade_salas:
        if ambiente[2][i] == 'Sujo':
            SujeiraDireitaMaisLonge_posicao = i
            SujeiraDireitaMaisLonge_distancia = i - PosicaoRobo

        i = i + 1
        
    
    i = PosicaoRobo
    while i >= 0 :
        if ambiente[2][i] == 'Sujo':
            SujeiraEsquerdaMaisLonge_posicao = i
            SujeiraEsquerdaMaisLonge_distancia = PosicaoRobo - i

        i = i - 1



    
    if (SujeiraDireitaMaisLonge_distancia < SujeiraEsquerdaMaisLonge_distancia) and (SujeiraDireitaMaisLonge_distancia != 0):

        #IR PARA A DIREITA PRIMEIRO DEPOIS IR PARA ESQUERDA
        i = PosicaoRobo
        while(i < SujeiraDireitaMaisLonge_posicao):
            key = 'd'
            aux, SujeiraNova = mover(key, ambiente)
            if(SujeiraNova == True):
                return "Refazer"
            
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1
        
        # i = SujeiraDireitaMaisLonge_posicao
        while(i > SujeiraEsquerdaMaisLonge_posicao):
            key = 'a'
            aux, SujeiraNova = mover(key, ambiente)
            if(SujeiraNova == True):
                return "Refazer"
            
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1



    elif (SujeiraEsquerdaMaisLonge_distancia < SujeiraDireitaMaisLonge_distancia) and (SujeiraEsquerdaMaisLonge_distancia != 0):

        #IR PARA A ESQUERDA DEPOIS PARA A DIREITA

        i = PosicaoRobo
        while(i > SujeiraEsquerdaMaisLonge_posicao):
            key = 'a'
            aux, SujeiraNova = mover(key, ambiente)
            if(SujeiraNova == True):
                return "Refazer"
            
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1
        
        while(i < SujeiraDireitaMaisLonge_posicao):
            key = 'd'
            aux, SujeiraNova = mover(key, ambiente)
            if(SujeiraNova == True):
                return "Refazer"
            
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1

    elif (SujeiraDireitaMaisLonge_distancia < SujeiraEsquerdaMaisLonge_distancia) and (SujeiraDireitaMaisLonge_distancia == 0): #IR PARA A ESQUERDA

        i = PosicaoRobo
        while(i > SujeiraEsquerdaMaisLonge_posicao):
            key = 'a'
            aux, SujeiraNova = mover(key, ambiente)
            if(SujeiraNova == True):
                return "Refazer"
            
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1



    elif (SujeiraEsquerdaMaisLonge_distancia < SujeiraDireitaMaisLonge_distancia) and (SujeiraEsquerdaMaisLonge_distancia == 0): #IR PARA A DIREITA

        i = PosicaoRobo   
        while(i < SujeiraDireitaMaisLonge_posicao):
            key = 'd'
            aux, SujeiraNova = mover(key, ambiente)
            if(SujeiraNova == True):
                return "Refazer"
            
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1

    return "Feito"


def automatico_base(ambiente):
    pos = encontrar_posicao_robo(ambiente)
    contador_esquerda = 0
    contador_direita = 0
    limpar(pos, ambiente)
    # limpar(pos, ambiente)
    for i in range (pos, 0, -1):
        contador_esquerda += 1
    for j in range (pos, quantidade_salas - 1, 1):
        contador_direita += 1
    
    #print(contador_direita)
    #print(contador_esquerda)
        
    if contador_direita < contador_esquerda:
        i = pos
        
        while(i < quantidade_salas - 1):
            key = 'd'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1
        while(i > 0):
            key = 'a'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1
    elif contador_esquerda < contador_direita:
        i = pos
        while(i > 0):
            key = 'a'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1
        while(i < quantidade_salas - 1):
            key = 'd'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1

def LimparTerminal():
    sistema_operacional = os.name

    # Verifique o sistema operacional para determinar o comando a ser usado
    if sistema_operacional == 'posix':  # Linux e macOS
        os.system('clear')
    elif sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:
        # Caso o sistema operacional não seja suportado, apenas imprima uma mensagem
        print("Limpeza de terminal não suportada para este sistema operacional.")

cleaning = True
Refazer = "refazer"

while cleaning:

    Salas = ['A','B','C','D','E','F','G','H','I','J']
    AspiradorDePo = ['','','','','','','','','','']
    Sujeira = ['','','','','','','','','','']
    base_de_ambiente = ['????', '????', '????', '????', '????', '????', '????', '????', '????', '????']

    ambiente = [Salas, AspiradorDePo, Sujeira, base_de_ambiente]

    print("\n===========================\n")
    quantidade_salas = int(input(" Digite a quantidade de Salas (max = 10): "))
    quantidade_salas_sujas = int(input (" Digite quantas salas sujas você quer (max <= quantidade de salas): "))
    tipo_de_ambiente = int(input("\n1. Base\n2. Onisciente\nQual vai ser o tipo de ambiente?: "))
    forma_de_pilotar = int(input("\n1. Automático\n2. Manual\nQual será o tipo de movimentação?: "))

    preencher_sala(quantidade_salas, quantidade_salas_sujas, ambiente)

    Debug = copy.copy(ambiente[2])

    RandomizarPosicaoRobo(ambiente, quantidade_salas)

    imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)

    print("\n\n")

    user_choice = (tipo_de_ambiente, forma_de_pilotar)

    match user_choice:
        
        case (1, 1): 
            automatico_base(ambiente)

        case (1, 2):
            while ambiente[3].index("????") != quantidade_salas:
                imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
                movimentar_robo = input("\nMovimente o robô com A ou D. Caso queira limpar, escreva 'limpar': ")
                quantidade_salas_sujas = mover_manual(movimentar_robo, ambiente, quantidade_salas_sujas)

        case (2, 1):
            while Refazer == "refazer":
                resultado = automatico_onisciente(ambiente, quantidade_salas)
                if resultado == "refazer":
                    Refazer = "refazer"
                else:
                    Refazer = "feito"

        case (2, 2):
            while quantidade_salas_sujas != 0:
                imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
                movimentar_robo = input("\nMovimente o robô com A ou D. Caso queira limpar, escreva 'limpar' ")
                quantidade_salas_sujas = mover_manual(movimentar_robo, ambiente, quantidade_salas_sujas)

    imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
    limpar_nova_sala = int(input("\n\n\n\n1. Sim\n2. Não\nDeseja limpar uma nova sala?: "))

    if limpar_nova_sala == 2:
        cleaning = False

    

# movimentar_robo = ''

# while movimentar_robo != 'x':
#     imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
#     movimentar_robo = input("\nMovimente o robô com A ou D : ")
#     mover_manual(movimentar_robo, ambiente)
    #LimparTerminal()
#automatico_onisciente(ambiente, quantidade_salas_sujas, quantidade_salas)
#automatico_base(ambiente, quantidade_salas_sujas)


        
        


