preco = float(input("Digite o preço do produto: "))
pagamento = int(input("Escolha uma opção de pagamento:\n1 - À vista em dinheiro, recebe 15% de desconto\n2 - À vista no cartão de crédito, recebe 10% de desconto\n3 - Em duas vezes, preço normal de etiqueta sem juros\n4 - Em três vezes, preço normal de etiqueta mais juros de 10%\n "))
if pagamento ==1:
    desconto=(preco*15)/100
    preco=preco-desconto
    print("Sua compra Ficou no valor de R$",preco)
if pagamento ==2:
    desconto=(preco*10)/100
    preco=preco-desconto
    print("Sua compra Ficou no valor de R$",preco)
if pagamento ==3:
    print("Sua compra Ficou no valor de R$",preco)
if pagamento ==4:
    desconto=(preco*10)/100
    preco=preco+desconto
    print("Sua compra Ficou no valor de R$",preco)
