# EMPAQUETADO EN TUPLAS
# ---------------------

numero = 3
cadena = 'benji'
booleano = False

# Empaquetamos valores en una tupla
tupla = numero, cadena, booleano

# Desempaquetamos los valores
_, b, _ = tupla
print(b)         # benji
print(tupla[1])  # benji