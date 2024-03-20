#Recebendo o valor
valorCompra = float(input('Olá, você recebeu um desconto de 15%, digite o valor da sua compra: '))

#fazendo o calculo
valorPorcentagem= (valorCompra*15)/100
valorFinal = valorCompra-valorPorcentagem

#Exibindo o resultado
print('Sua compra ficou no total de: R$',valorFinal,', voce recebeu R$',valorPorcentagem,'de desconto.')