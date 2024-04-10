import random
faces = int(input("Insira o número de faces que voçê quer: 4,6,8,10,12 ou 16: "))
sorteio = random.randint(1,faces)
if faces<17 and faces>3 and faces !=14 and faces%2==0:
 print("O número sorteado foi: ",sorteio)
else:
 print("Número de faces invalido")