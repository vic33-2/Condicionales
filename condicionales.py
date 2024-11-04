'''
Condiciales if:
    Evalua expresiones booleanas

Esructura:
    if expresion:
        instrucciones

    if expresion:
        instrucciones
    else: 
        instrucciones

    if expresion:
        instrucciones 
    elif expresion:
        instrucciones
    else:
        instrucciones  
'''

print('Programa que verifica si un numero es posotivo')
num = int(input('Ingrese un numero: '))
# preguntar el numero mayor a 0:
if num > 0:
    print('El numero es psitivo')
else:
  print('El numero es negativo')
print('Fin del programa')   
