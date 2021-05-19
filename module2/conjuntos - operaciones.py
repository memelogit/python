# OPERACIONES
# -----------

A = {2, 3}
B = {3, 4}

# Intersección
print('intersección:', A & B)

# Unión
print('unión:', A | B)

# Diferencia
print('Diferencia:', A - B)
print('Diferencia:', B - A)

# Complemento de A
U = {1} | A | B
print('Complemento de A:', U - A)

# Diferencia simétrica
print('Diferencia simétrica:', A ^ B)