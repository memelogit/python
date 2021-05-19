# OPERACIONES
# -----------

import numpy as np

arreglo = np.array([2, 3, 9, 4, 6, 7, 2, 1])

# Operaciones básicas
print('suma:', 2 + arreglo)
print('resta:', 2 - arreglo)
print('multiplicación:', 2 * arreglo)
print('división:', 2 / arreglo)

# Operaciones complejas
print('raíz cuadrada:', np.sqrt(arreglo))
print('exponente:', np.sqrt(arreglo))
print('logaritmo:', np.log(arreglo))
print('seno:', np.sin(arreglo))
print('coseno:', np.cos(arreglo))

# Operaciones con matrices
matriz = np.matrix([[1, 2], [3, 4]])
print('suma:', matriz + matriz)
print('producto punto:', matriz.dot(matriz))
print('transpuesta', matriz.T)