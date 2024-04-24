def abrirCaixa():
    import random
    probabilidade = random.randint(1,100)
    if probabilidade>0 and probabilidade<=80:
        print("Você coletou 1 item comum!")
        return
    if probabilidade>=81 and probabilidade<=99:
        print("Você coletou 1 item raro!")
        return
    if probabilidade==100:
        print("Você coletou 1 item Lendário!")
        return
menu= int(input("Escolha uma opção:\n1-Abrir uma caixa\n2-Consultar itens\n0-Sair"))

comum=0
raro=0
lendario=0

while menu!=0:
    if menu==1:
        
