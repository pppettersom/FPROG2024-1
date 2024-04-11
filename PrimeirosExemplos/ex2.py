##########FUNções###############
def tabuada(n):
    for i in range(1,11):
        conta=n*i
        print(n,"x",i,"= ",conta)


#########PRINCIPAL###########

#numero = int(input("Digite o número para multiplicar: "))
#tabuada(numero)


for i in range(1,11):
    tabuada(i)
    print("------------------")