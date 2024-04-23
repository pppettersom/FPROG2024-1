
opcao='s'
resultado=1
while opcao=='s':
    numero = int(input("Entre com um número: "))
    for n in range(1,numero+1):
        resultado = n*resultado
    print("O fatorial de ",numero," é ",resultado)
    resultado=1
    opcao = input("Calcular outro número (s/n)? ")