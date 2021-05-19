# LISTAS
# ------

# Creando listas
lst1 = [2, 4, 6, 8, 10]
lst2 = ['hugo', 'paco', 'luis']
lst3 = [lst1, lst2]

# Primer elemento
print(lst1[0])

# Último elemento
print(lst1[-1])

# Modificando segundo elemento
lst1[1] = -4
print(lst1)

# Acceso a listas anidadas
print(lst3[1][1])

# Accediento a sub-lista
print(lst1[1:3]) # [4, 6]
print(lst1[3:])  # [8, 10]
print(lst1[::2]) # [2, 6, 10]