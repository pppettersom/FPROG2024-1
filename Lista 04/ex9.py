quant=int(input("Entre com um número: "))
caracter = input("Entre com um caracter :")

for n in  range(0,quant+1):
    for x in range(n):
        print(caracter,end=" ")
    print()
