def sorteio(inicio,fim):
    import random
    numeroSort=random.randint(inicio,fim)
    return numeroSort

inicio=int(input("Digite o número inicial para o intervalo do sorteio: "))
fim=int(input("Digite o número final para o intervalo do sorteio: "))
resultado=sorteio(inicio,fim)
print("O número sorteado é: ",resultado)