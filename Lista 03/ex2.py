numA = int(input("Digite o número A:"))
numB = int(input("Digite o número B:"))
numC = int(input("Digite o número C:"))

soma1 = numA+numB
soma2 = numA+numC

if(soma1<soma2):
    print("A+B é menor que A+C")
else:
    print("A+B é maior que A+C")