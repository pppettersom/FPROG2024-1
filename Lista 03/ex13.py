#Recebendo os dados
grauA= float(input('Olá, digite sua nota do Grau A: '))
grauB= float(input('Digite sua nota do Grau B: '))

#Fazendo o cálculo
somaMedia= (grauA+(2*grauB))/3

#Mostrando o resultado
print('A sua média é: ',somaMedia)

if somaMedia>=6:
    print("Você foi aprovado por média!")
if somaMedia<6:
    print("Você está de recuperação")
    opcao=input("Você quer substituir o grau A ou grau B?")
    grauC= float(input("Insira a nota do Grau C: "))
    if opcao == 'A':
        somaMedia= (grauC+(2*grauB))/3
        if somaMedia>=6:
            print("Você foi aprovado ! sua média é:",somaMedia)
        else:
            print("Você foi reprovado ! sua média é:",somaMedia)
    
    if opcao == 'B':
        somaMedia= (grauA+(2*grauC))/3
        if somaMedia>=6:
            print("Você foi aprovado ! sua média é:",somaMedia)
        else:
            print("Você foi reprovado ! sua média é:",somaMedia)