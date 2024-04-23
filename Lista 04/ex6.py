import random
somaSort=0
for n in range(0,5):
    sorteado = random.randint(0,100)
    if n ==0:
        menor=sorteado
        maior=sorteado
    if sorteado<menor:
        menor=sorteado
    if sorteado>maior:
        maior=sorteado
    somaSort=sorteado+somaSort

print("O menor número sorteado foi: ",menor," E o maior número sorteado foi: ",maior)
print("A média dos números sorteados é: ",somaSort/5)
    