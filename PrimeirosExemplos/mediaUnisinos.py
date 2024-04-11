def mediaUnisinos(grauA,grauB):
    media = (grauA+(2*grauB))/3.0
    return media


grauA=float(input("Digite a nota do grau A: "))
grauB=float(input("Digite a nota do grau B: "))

grauFinal = mediaUnisinos(grauA,grauB)
print(grauFinal," é a sua média")