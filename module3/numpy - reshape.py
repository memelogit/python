# RESHAPE
# -------

import numpy as np

arreglo = np.array([2, 3, 9, 4, 6, 7, 2, 1, 0])
print(arreglo.shape)

# transforma el arreglo 9, en uno de 3x3
arreglo = arreglo.reshape(3,3)
print(arreglo.shape)
print(arreglo)