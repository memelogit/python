# ACTIVIDAD
# ---------

# Implementa el producto Cartesiano 𝐴 𝑋 𝐵 e imprímelo en consola
# Usa compresión de conjuntos

A = {2,3,4}
B = {1,2}
producto = {(a, b) for a in A for b in B}
print(producto)