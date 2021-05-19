# SETS
# ----

# Creación de un conjunto
colores = {'azul', 'rojo', 'blanco', 'blanco'}

# Eliminamos valores repetidos
tupla = 1, 1, 2, 3, 4, 3, 5, 6, 7, 7, 6
conjunto =  set(tupla)  # casting a set
print(tuple(conjunto))  # casting a tupla

# En una sola linea
# nota que se estan usando dobles paréntesis
print(tuple(set((1, 1, 2, 3, 4, 3, 5, 6, 7, 7, 6))))

# No es posible acceder a los elementos
print(conjunto[2])