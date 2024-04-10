valorProd= float(input("Digite o valor do produto: "))

if valorProd<20:
    lucro=(valorProd*45)/100
    valor=valorProd+lucro
    print("O valor do produto ficará: ",valor)
elif valorProd<50 and valorProd>20:
    lucro=(valorProd*35)/100
    valor=valorProd+lucro
    print("O valor do produto ficará: ",valor)
elif valorProd>50:
    lucro=(valorProd*25)/100
    valor=valorProd+lucro
    print("O valor do produto ficará: ",valor)