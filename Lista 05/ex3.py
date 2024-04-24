def nota(grauA,grauB):
    somaMedia= (grauA+(2*grauB))/3

    if somaMedia>=6:
        print("APROVADO")
    if somaMedia<6:
        print("REPROVADO")
        opcao=input("Você quer substituir o grau A ou grau B? ")
        opcao=opcao.lower()
        grauC= float(input("Insira a nota do Grau C: "))
        if opcao == 'a':
            somaMedia= (grauC+(2*grauB))/3
            if somaMedia>=6:
                print("APROVADO")
            else:
                print("REPROVADO")
        
        if opcao == 'b':
            somaMedia= (grauA+(2*grauC))/3
            if somaMedia>=6:
                print("APROVADO")
            else:
                print("REPROVADO")

grauA= float(input('Digite sua nota do Grau A: '))
grauB= float(input('Digite sua nota do Grau B: '))
nota(grauA,grauB)