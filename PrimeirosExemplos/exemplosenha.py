senhaUsuario = '123'
senhaDigitada = ''
cont=0
senha = False

while cont<3 and senha==False:

    senhaDigitada = input("Digite a senha:")

    if(senhaUsuario==senhaDigitada):
        print("Você entrou no sistema")
        senha = True
        cont = 3

    elif(senhaDigitada!=senhaUsuario):
        if(cont<2):
            print("Você errou a senha! Ainda restam",3-cont-1,"Tentativas")
            senha = False
            cont = cont+1
        else:
            print("você errou a senha, tentativas esgotadas!")
            cont=3