import random

escolhaUser = input("Escreva se quer PAR ou IMPAR ")
numUser = int(input("Escolha um número de 0 a 5 "))


if escolhaUser == "PAR":
    sorteio=random.randint(0,5)
    resultado=numUser+sorteio
    if resultado%2==0:
        print("Você venceu!, o seu número escolhido foi",numUser,"e o número da maquina foi",sorteio,"A soma desse números é par!")
    else:
        print("Você perdeu!, o seu número escolhido foi",numUser,"e o número da maquina foi",sorteio,"A soma desse números é impar!")

elif escolhaUser =="IMPAR":
    sorteio=random.randint(0,5)
    resultado=numUser+sorteio
    if resultado%2==0:
        print("Você perdeu!, o seu número escolhido foi",numUser,"e o número da maquina foi",sorteio,"A soma desse números é par!")
    else:
        print("Você venceu!, o seu número escolhido foi",numUser,"e o número da maquina foi",sorteio,"A soma desse números é impar!")

else:
    print("Opção invalida")