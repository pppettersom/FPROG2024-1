
#Variáveis genéricas que podem ser trocadas facilmente sem alterar o código

#Pergunta
pergunta = 'Qual é o verdadeiro nome do super-herói Batman?'


#Alternativas
altA = 'a) Bruce Wayne'
altB = 'b) Clark Kent'
altC = 'c) Peter Parker '
altD = 'd) Tony Stark '
altE = 'e) Steve Rogers '

#Armazenando a resposta correta
resposta = altA

#Fazendo a pergunta
print(pergunta)
#dando as alternativas
print(altA)
print(altB)
print(altC)
print(altD)
print(altE)
#armazenando a resposta do usuário
respostaUser = input(': ')

#Mostrando os resultados
print('Você respondeu a alternativa',respostaUser,', a resposta correta era a alternativa',resposta)