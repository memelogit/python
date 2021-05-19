# ACCESO A TUPLAS
# ---------------

# Tupla usando coma
tupla = 'ITESO',
print(type(tupla))

# Tupla usando paréntesis
tupla = ('ITESO', 2021)
print(type(tupla))

# Acceso al último elemento
print(tupla[-1])

# Error al modificar una tupla
tupla[0] = 'iteso'