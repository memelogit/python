# ACTIVIDAD
# ---------

# 1.- Escribir un programa que pida al usuario dos números y muestret
# por pantalla su división. Si el divisor es cero el programa debe
# mostrar un error

n = float(input('Introduce el dividendo: '))
m = float(input('Introduce el divisior: '))
if m == 0:
    print('¡Error! No se puede dividir por 0.')
else:
    print(n/m)

# 2.- Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es par o impar

n = int(input('Introduce un número entero: '))
if n % 2 == 0:
    print('El número ' + str(n) + ' es par')
else:
    print('El número ' + str(n) + ' es impar')