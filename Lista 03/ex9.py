vDolar = float(input("Digite a cotação atual do dólar em reais: "))
vEuro =float(input("Digite a cotação atual do euro em reais: "))
escolha = int(input("-----Faça sua escolha:-----\n 1) Converter de Real para Euro\n 2) Converter de Real para Dólar\n 3) Converter de Euro para Dólar\n 4) Converter de Euro para Real\n 5) Converter de Dólar para Euro\n 6) Converter de Dólar para Real\n"))

if escolha ==1:
    valor = float(input("Digite o valor a ser convertido: "))
    vFinal=valor/vEuro
    print("Você terá o valor: ",vFinal)

elif escolha ==2:
    valor = float(input("Digite o valor a ser convertido: "))
    vFinal=valor/vDolar
    print("Você terá o valor: ",vFinal)
elif escolha ==3:
    valor = float(input("Digite o valor a ser convertido: "))
    vFinal=(vEuro/vDolar)*valor
    print("Você terá o valor: ",vFinal)
elif escolha ==4:
    valor = float(input("Digite o valor a ser convertido: "))
    vFinal=vEuro*valor
    print("Você terá o valor: ",vFinal)
elif escolha ==5:
    valor = float(input("Digite o valor a ser convertido: "))
    vFinal=(vDolar/vEuro)*valor
    print("Você terá o valor: ",vFinal)
elif escolha ==6:
    valor = float(input("Digite o valor a ser convertido: "))
    vFinal=valor*vDolar
    print("Você terá o valor: ",vFinal)
else:
    print("opção invalida")
