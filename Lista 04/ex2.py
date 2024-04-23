import random

sorteado = random.randint(1,10)
chance = 0
while chance<3:
    adivinha = int(input("Tente adivinhar o número de 1 a 10: "))
    if adivinha == sorteado:
        print("Você acertou! o número é: ",sorteado)
        chance =3
    elif adivinha>sorteado:
        print("O número que você digitou é maior!")
        chance = chance+1
    elif adivinha<sorteado:
        print("O número que você digitou é menor!")
        chance = chance+1
print("O número era: ",sorteado)