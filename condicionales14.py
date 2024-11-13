mes = int(input("igresa un numero de mes (1-12): "))
if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes ==8 or mes ==10 or mes ==12:
    print("este mes tien 31 dias.")
elif mes == 4 or mes ==6 or mes ==9 or mes ==11:
    print("este mes tiene 30 dias.")
elif mes == 2:
    print("este mes tiene 28 dias o 29 dias si es ano bisiesto.") 
else:
    print("Error: el numero de mes es incorrecto.")    