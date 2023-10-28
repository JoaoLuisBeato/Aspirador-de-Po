import random
import os

def imprimir_tabela(matrix, tipo_ambiente, quantidade_salas):

    for row in range(len(matrix)):
        for item in matrix[row][:quantidade_salas]:
            print(item, end='\t') # Escreve o valor como não descoberto
        print()  # Pule para a próxima linha após cada linha da matriz
    
    for item in Debug[:quantidade_salas]:
        print(item, end='\t') # Escreve o valor como não descoberto
        


    


def RandomizarPosicaoRobo(AspiradorDePo, quantidade_salas):
    # Verifica se o Robô está na lista já e apaga pra ser trocado
    for i in range(0, quantidade_salas):
        if AspiradorDePo[1][i] == 'Robo':
            AspiradorDePo = ''
    
    # Gera um número aleatório entre 0 - 9
    random_integer = random.randint(0, quantidade_salas - 1)
    print(quantidade_salas)

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
    

def mover_manual(input, ambiente):
    pos = encontrar_posicao_robo(ambiente)

    if input == 'd' and pos + 1 <= quantidade_salas - 1:
        ambiente[1][pos] = ''
        ambiente[1][pos + 1] = 'Robo'
    elif input == 'a' and pos - 1 >= 0:
        ambiente[1][pos] = ''
        ambiente[1][pos - 1] = 'Robo'
    elif input == 'limpar':
        limpar(pos, ambiente)
    return
    

def automatico_onisciente(ambiente, quantidade_sujeira, quantidade_salas):
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
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1
        
        # i = SujeiraDireitaMaisLonge_posicao
        while(i > SujeiraEsquerdaMaisLonge_posicao):
            key = 'a'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1



    elif (SujeiraEsquerdaMaisLonge_distancia < SujeiraDireitaMaisLonge_distancia) and (SujeiraEsquerdaMaisLonge_distancia != 0):

        #IR PARA A ESQUERDA DEPOIS PARA A DIREITA

        i = PosicaoRobo
        while(i > SujeiraEsquerdaMaisLonge_posicao):
            key = 'a'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1
        
        while(i < SujeiraDireitaMaisLonge_posicao):
            key = 'd'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1

    elif (SujeiraDireitaMaisLonge_distancia < SujeiraEsquerdaMaisLonge_distancia) and (SujeiraDireitaMaisLonge_distancia == 0): #IR PARA A ESQUERDA

        i = PosicaoRobo
        while(i > SujeiraEsquerdaMaisLonge_posicao):
            key = 'a'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i - 1



    elif (SujeiraEsquerdaMaisLonge_distancia < SujeiraDireitaMaisLonge_distancia) and (SujeiraEsquerdaMaisLonge_distancia == 0): #IR PARA A DIREITA

        i = PosicaoRobo   
        while(i < SujeiraDireitaMaisLonge_posicao):
            key = 'd'
            mover(key, ambiente)
            imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
            i = i + 1

    return 'Forster Sniper'


def automatico_base(ambiente, quantidade_sujeira):
    pos = encontrar_posicao_robo(ambiente)
    # limpar(pos, ambiente)
    while pos > 0:
        key = 'a'
        if mover(key, ambiente):
            quantidade_sujeira -= 1

        imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
        pos -= 1

    while pos < quantidade_salas:
        key = 'd'
        if mover(key, ambiente):
            quantidade_sujeira -= 1
        
        imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
        pos += 1
    return 'burro'


def LimparTerminal():
    os.system('cls')

if __name__ == "__main__":
    
    Salas = ['A','B','C','D','E','F','G','H','I','J']
    AspiradorDePo = ['','','','','','','','','','']
    Sujeira = ['','','','','','','','','','']
    base_de_ambiente = ['????', '????', '????', '????', '????', '????', '????', '????', '????', '????']

    ambiente = [Salas, AspiradorDePo, Sujeira, base_de_ambiente]


    print("\n===========================\n")
    quantidade_salas = int(input(" Digite a quantidade de Salas (max = 10): "))
    quantidade_salas_sujas = int(input (" Digite quantas salas sujas você quer (max <= quantidade de salas): "))
    tipo_de_ambiente = int(input("\n1. Base\n2. Onisciente\nQual vai ser o tipo de ambiente?: "))

    Debug = (preencher_sala(quantidade_salas, quantidade_salas_sujas, ambiente))[2]

    RandomizarPosicaoRobo(ambiente, quantidade_salas)
    imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
    print("\n\n\n\n\n")

    movimentar_robo = ''

    while movimentar_robo != 'x':
        imprimir_tabela(ambiente, tipo_de_ambiente, quantidade_salas)
        movimentar_robo = input("\nMovimente o robô com A ou D : ")
        mover_manual(movimentar_robo, ambiente)
        #LimparTerminal()
    #automatico_onisciente(ambiente, quantidade_salas_sujas, quantidade_salas)
    #automatico_base(ambiente, quantidade_salas_sujas)
        
        


