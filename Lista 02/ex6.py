print('----TECHMUNDO----')

#Pegando as quantidades
quantS = int(input('Quantos smartphones foram vendidos hoje?'))
quantT = int(input('Quantos tablets foram vendidos hoje?'))


#Fazendo a soma de quantos smartphones e tablets foram vendidos
somaS = quantS*1000
somaT = quantT*1500

#fazendo a soma de todas as vendas do dia
somaTudo = somaS+somaT


#Exibindo os resultados

print('O total vendido em Smartphones foi: R$',somaS,'e o total vendido em tablets foi: R$',somaT)
print('---- O TOTAL VENDIDO HOJE FOI: R$',somaTudo,'----')