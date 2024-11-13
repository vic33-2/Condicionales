num1 = int(input("introduce el primer numero: "))
num2 = int(input("introduce el segundo numero: "))
num3= int(input("introduce el tercer numero: "))
numeros = [num1,num2,num3]
numeros.sort(reverse=True)
print("los numeros ordenados de mayor a menor son:", numeros)