# MÉTODOS DE CONJUNTOS
# --------------------

A = {2, 3}
B = {3, 4}
U = {1} | A | B

# Intersección
print('intersección:', A.intersection(B))

# Unión
print('unión:', A.union(B))

# Diferencia
print('Diferencia:', A.difference(B))
print('Diferencia:', B.difference(A))

# Es un subset, A contenido en U
print('A subset de U:', A.issubset(U))

# Diferencia simétrica
print('Diferencia simétrica:', A.symmetric_difference(B))