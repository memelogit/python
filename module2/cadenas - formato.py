# FORMATO DE CADENAS
# ------------------

# Accediendo argumentos por posición
print('{1} {0} {2}'.format('a', 'b', 'c'))
print('{0}{1}{0}'.format('abra', 'cad'))

# Accediendo argumentos por nombre
print('{clave}={valor}'.format(
    clave='nombre',
    valor='Victor'
))

# Alinear el texto y especificar el ancho
print('{:<80}'.format('izquierda'))
print('{:>80}'.format('derecha'))
print('{:^80}'.format('centrado'))
print('{:*^80}'.format('centrado'))

# Valor a diferentes bases:
print('int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}'.format(12))