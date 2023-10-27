import random

def preencher_sala(quantidade_salas, quantidade_salas_sujas, ambiente):
    if(quantidade_salas < quantidade_salas_sujas):
        print("Quantidade maior de sujeiras do que salas")
        return 0


    while quantidade_salas_sujas != 0:
        random_integer = random.randint(0, quantidade_salas - 1)
        if(ambiente[2][random_integer] == ''):
            ambiente[2][random_integer] = 'SUJEIRA'
            quantidade_salas_sujas = quantidade_salas_sujas - 1
        else:
            continue
    print(ambiente)
    return ambiente


Salas = ['A','B','C','D','E','F','G','H','I','J']
AspiradorDePo = ['','','','','','','','','','']
Sujeira = ['','','','','','','','','','']

ambiente = [Salas, AspiradorDePo, Sujeira]



print("\n===========================\n")
quantidade_salas = int(input(" Digite a quantidade de Salas (max = 10): "))
quantidade_salas_sujas = int(input (" Digite quantas salas sujas você quer (max <= quantidade de salas): "))

preencher_sala(quantidade_salas, quantidade_salas_sujas, ambiente)

