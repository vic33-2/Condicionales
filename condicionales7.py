base =  int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
num = abs(exponente)
if exponente == 0 :
    print("el resultado de la potencia es: 1")
else:
    if exponente > 0:
        print(f"el resultado de la potencia es: {base**exponente}")
    else:
        print(f"el resultado de la potencia es: {base**num}")
print("fin del programa")