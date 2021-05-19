# METODOS DE CADENAS
# ------------------

cadena = 'ANita Lava la Tina'

print('minusculas:', cadena.lower())
print('mayusculas:', cadena.upper())
print('capitalizacion:', cadena.capitalize())
print('invertir case:', cadena.swapcase())
print('titulo:', cadena.title())
print('remplazo:', cadena.replace('la', 'una'))
print('a lista:', cadena.split(' '))
print('total letra A:', cadena.count('a'))
print('index de lava:', cadena.find('Lava'))

# Comparación
if cadena.startswith('A'):
    print('comienza con A')
if cadena.endswith('a'):
    print('termina con a')
print('314 es digito?' ,'314'.isdigit())
print('gato es digito?' ,'gato'.isdigit())
print('g^ato es alfanumerico?' ,'g^ato'.isalnum())