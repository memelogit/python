# ACTIVIDAD
# ---------

# Escribe una función que convierta grados Celcius
# a Fahrenheit. Después aplica la función a la siguiente
# lista de valores

lista = [-2.6, 1.8, 3.4, 9.65, 15.2]

def fahrenheit(celcius:float) -> float:
    return 9/5 * celcius + 32

print(list(map(fahrenheit, lista)))