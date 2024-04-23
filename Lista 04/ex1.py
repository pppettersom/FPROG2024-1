import random
## escrever todos os números de 1 a 100
print("Números inteiros de 0 a 100")
for n in range(0,101):
    print(n)

##escrever números pares de 1 a 50
print("Números pares de 20 a 50")
for nPar in range(20,51):
    
    if nPar%2==0:
        print(nPar)

##Números inteiros entre 25 e 70 em ordem decrescente
print("Números inteiros entre 25 e 70 em ordem decrescente")
for nDec in range(70,24,-1):
    print(nDec)

##Números ímpares entre 25 e 95 em ordem decrescente
print("##Números ímpares entre 25 e 95 em ordem decrescente")
for nImp in range (95,24,-1):
    if nImp%2!=0:
        print(nImp)

##Ler 15 números e escrever a soma e a média
print("Ler 15 números e escrever a soma e a média")
cont = 0
somaNum = 0.0
while cont<15:
    num = float(input("Digite o número:"))
    somaNum = num+somaNum
    cont = cont+1
mediaNum=somaNum/15
print("A soma dos números é: ",somaNum,"\n A média dos números somados é: ",mediaNum)
##Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos.
print("Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos.")
cont2 = 0
par = 0
impar = 0
while cont2<10:
    numero = int(input("Digite um número: "))
    if numero%2==0:
        par = par+1
        cont2 = cont2+1
    else:
        impar = impar+1
        cont2 = cont2+1
print("Números pares: ",par,"\n Números ímpares: ",impar)

##Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem “POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de números positivos e negativos lidos.
pos = 0
neg = 0
null = 0
for sorteio in range(0,20):
    num = random.randint(-10,10)
    if num>0:
        print(num, "POSITIVO")
        pos = pos+1
    elif num<0:
        print(num, "NEGATIVO")
        neg = neg+1
    elif num==0:
        print(num, "NULO")
        null = null+1
print("Números Positivos: ",pos,"\nNúmeros negativos: ",neg,"\nNulo: ",null)

##Ler n números e imprimir no final a soma dos números lidos
print("Ler n números e imprimir no final a soma dos números lidos")
quant = int(input("Digite quantos números vão ser lidos: "))
soma=0
while quant>0:
    numSoma=float(input("Digite o número a somar: "))
    soma = numSoma+soma
    quant = quant-1
print("A soma dos números é: ",soma)

