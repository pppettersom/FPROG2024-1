opcao='s'
while opcao == 's':
    numero= int(input("Entre com um número: "))
    for n in range(1,11):
        print(numero,"X",n,"=",numero*n)
    opcao=input("Calcular outro número (s/n)?") 