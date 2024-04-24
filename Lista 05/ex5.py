def somar(n1,n2):
    resultado=n1+n2
    return resultado
def subtrair(n1,n2):
    resultado=n1-n2
    return resultado
def multiplicar(n1,n2):
    resultado=n1*n2
    return resultado
def dividir(n1,n2):
    resultado=n1/n2
    return resultado

opcao=int(input("Escolha uma opção:\n1) Somar\n2)Subtrair\n3)Multiplicar\n4)Dividir\n"))

if opcao==1:
    n1=float(input("Digite o primeiro número a somar: "))
    n2=float(input("Digite o segundo número a ser somado: "))
    resultado=somar(n1,n2)
    print("O resultado é: ",resultado)
elif opcao==2:
    n1=float(input("Digite o primeiro número: "))
    n2=float(input("Digite o número que será diminuído: "))
    resultado=subtrair(n1,n2)
    print("O resultado é: ",resultado)
elif opcao==3:
    n1=float(input("Digite o primeiro número a multiplicar: "))
    n2=float(input("Digite o segundo número a ser multiplicado: "))
    resultado=multiplicar(n1,n2)
    print("O resultado é: ",resultado)
elif opcao==4:
    n1=float(input("Digite o primeiro número: "))
    n2=float(input("Digite o número a ser dividido: "))
    if n2==0:
        print("Não é possível dividir por 0!")
    else:
        resultado=dividir(n1,n2)
        print("O resultado é: ",resultado)
else:
    print("Oção Inválida")