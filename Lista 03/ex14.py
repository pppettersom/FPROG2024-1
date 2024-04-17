idade = int(input("Olá, digite a sua idade"))
dependente = input("Você tem algum dependente? S/N ")
valorTotal = 300
if dependente=='S':
    quantDep = int(input("Insira a quantidade de dependentes: "))
    while quantDep!=0:
        idadeDep = int(input("Insira a idade do dependente"))
        if idadeDep<=10:
            valor = 400
            valorTotal = valorTotal+valor
        if idadeDep>10 and idadeDep<=30:
            valor = 520
            valorTotal = valorTotal+valor
        if idadeDep>=31 and idadeDep<60:
            valor = 695
            valorTotal = valorTotal+valor
        if idadeDep>60:
            valor = 780
            valorTotal = valorTotal+valor
        quantDep=quantDep-1
    print("O seu plano vai ficar no valor de: R$",valorTotal)
elif dependente=='N':
    print("O seu plano vai ficar no valor de: R$",valorTotal)
else:
    print("Opção Inválida")

        

    
    