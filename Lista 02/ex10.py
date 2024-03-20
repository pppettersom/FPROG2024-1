#Recebendo as quantidades
quantCamiseta = int(input('Olá, quantas camisetas fora compradas?'))
quantCalca = int(input('Quantas calças fora compradas?'))
quantCinto = int(input('Quantos cintos fora comprados?'))

#fazendo o calculo
totalCamiseta = quantCamiseta*25
totalCalca = quantCalca*100
totalCinto = quantCinto*40

valorCompra = totalCamiseta+totalCalca+totalCinto
valorPorcentagem= (valorCompra*10)/100
valorFinal = valorCompra-valorPorcentagem

#Exibindo o resultado
print('Sua compra ficou no total de: R$',valorFinal,', voce recebeu R$',valorPorcentagem,'de desconto.')