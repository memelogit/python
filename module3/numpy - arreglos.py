# ARREGLOS
# --------

import numpy as np

# Creacion de arreglos
arreglo = np.array([3, 5, 7, 9])
matriz = np.array([[1, 2, 3],[9, 8, 7]])
print(type(arreglo))

# Crea un arreglo usando una secuencia
print(np.arange(0, 9, 3))

# Arreglo de zeros 5 filas 4 columnas
print(np.zeros([5, 4]))

# Arreglo de unos
print(np.ones(6))

# Dividir uniformemente un rango
print(np.linspace(0, 1.0, 6))

# Arreglo identidad
print(np.eye(5))

# Números aleatorios, arreglo de dos elementos
print(np.random.rand(2))

# Números aleatorios, valor entre limites
print(np.random.randint(0, 100))