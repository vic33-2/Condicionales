nota = int(input("Introduce la nota: "))
edad = int(input)("Introduce la edad: ")
sexo = int(input("Introduce el sexo: "))
if nota >= 5 and edad >= 19:
    if sexo == 'M':
        print('ACEPTADO')
    elif sexo =='F':
        print('Posible')
    else:
        print("NO ACPETADO.")
else:
    print("NO ACPETADO.")    