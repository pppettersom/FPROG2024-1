for n in range(2,100):
        primo = True
        for i in range(2,int(n/2)+1):
            if n%i ==0:
                primo=False
                break
        if primo==True:
             print(n)
             
soma=0
for n in range(1,11):
    soma=soma+n
print("A soma de 1 até 10 é: ",soma) 

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

resultado=1
for n in range(1,5+1):
    resultado = n*resultado
print("O fatorial de 5 é ",resultado)

count = 0
num = 1
while count < 5:
    if num % 2 == 0 and num % 5 == 0:
        print(num)
        count += 1
    num += 1