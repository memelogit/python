# SUBCONJUNTOS
# -----------

A = {2, 3}
B = {3, 4}
U = {1}

# Unión como método
U = U.union(A).union(B)

# Preguntamos si es un si {2, 4} es subconjunto de U
print({2, 4} <= U)

# Preguntamos si B es subconjunto de A
print(B <= A)

# Preguntamos si {1, 2, 3, 4} es subconjunto de U
print({1, 2, 3, 4} <= U)