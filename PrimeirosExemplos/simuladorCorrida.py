import random

posHamster1 = 0
posHamster2 = 0

# o-ninguem venceu 
#1- hamster1 venceu 
#2 hamster3 venceu 
#3- empate
vencedor = 0 
while vencedor==0 : #Continua a corrida
    #Fazendo a movimentação do hamster 1
    nroSorteado = random.randint(1,5) # Sorteia entre 1 e 5
    #Aplicar as regras da tabela na posição do hamster 1
    if nroSorteado == 1:
        posHamster1 = posHamster1+1
    elif nroSorteado == 2:
        posHamster1 = posHamster1+2
    elif nroSorteado == 3:
        pass
    elif nroSorteado == 4:
        posHamster1=posHamster1-1
    else:
        posHamster1=posHamster1-2
    #Garantir que não existe posição negativa nem maior que 12
    if posHamster1 < 0:
        posHamster1=0
    if posHamster1>12:
        posHamster1=12

    #Fazendo a movimentação do hamster 2
    nroSortead = random.randint(1,5) # Sorteia entre 1 e 5
    #Aplicar as regras da tabela na posição do hamster 1
    if nroSorteado == 1:
        posHamster2 = posHamster2+1
    elif nroSorteado == 2:
        posHamster2 = posHamster2+2
    elif nroSorteado == 3:
        pass
    elif nroSorteado == 4:
        posHamster2=posHamster2-1
    else:
        posHamster2=posHamster2-2
    #Garantir que não existe posição negativa nem maior que 12
    if posHamster2 < 0:
        posHamster2=0
    if posHamster2>12:
        posHamster2=12

    #Testa quem venceu
    if posHamster1==12:
        vencedor=1 #hamster 1 venceu

    if posHamster2==12:

        if vencedor==0:
            vencedor=2 #hamster 2 venceu

    else:
        vencedor = 3 #empate

#imprime na tela o status da corrida
    print('Hamster 1: ')
    for n in range(posHamster1):
        print('*',end=' ')
    print()#Quebra de linha

    print('Hamster 1: ')
    for n in range(posHamster1):
        print('*',end=' ')
    print()#QUebra de linha

#imprimir quemm ganhou
if vencedor==1:
    print("Hamster 1 venceu")
elif vencedor==2:
    print("Hamster 2 venceu")
else:
    print("Empate")



    

