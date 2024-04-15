valor=int(input("Digite o valor: "))
if valor>0:
    if valor>=100:
        n100=valor //100
        valor = valor%100
        print(n100,"nota(s) de 100")
    if valor>=50:
        n100=valor //50
        valor = valor%50
        print(n100,"nota(s) de 50")
    if valor>=20:
        n100=valor //20
        valor = valor%20
        print(n100,"nota(s) de 200")
    if valor>=10:
        n100=valor //10
        valor = valor%10
        print(n100,"nota(s) de 10")
    if valor>=5:
        n100=valor //5
        valor = valor%5
        print(n100,"nota(s) de 5")
    if valor>=1:
        n100=valor //1
        valor = valor%1
        print(n100,"nota(s) de 1")

