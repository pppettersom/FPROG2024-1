##########FUNÇÕES#########
def cumprimentar(nome):
    print("Olá,",nome,"!")



#########PROGRAMA PRINCIPAL###########
#nome1=input("Usuário 1, Digite seu nome: ")
#cumprimentar(nome1)

#nome2=input("Usuário 2, Digite seu nome: ")
#cumprimentar(nome2)

for i in range(5):
    print("Usuário",i+1, end= " ")
    nome=input("Digite seu nome: ")
    cumprimentar(nome)