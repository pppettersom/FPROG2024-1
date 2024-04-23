divisor = int(input("Entre com o valor do divisor: "))
intervaloInicio = int(input("Início do intervalo: "))
intervaloFinal = int(input("Final do intervalo: "))
print("Números divisíveis por",divisor,"no intervalo de",intervaloInicio,"a",intervaloFinal)
for n in range  (intervaloInicio,intervaloFinal):
    if n%3==0:
        print(n, end=" ")

