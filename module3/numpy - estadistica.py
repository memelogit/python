# METODOS DE ESTADISTICA
# ----------------------

import numpy as np

arreglo = np.array([2, 3, 9, 4, 6, 7, 2, 1])

# Estadística
print('suma:', np.mean(arreglo))
print('mediana:', np.median(arreglo))
print('varianza:', np.var(arreglo))
print('desviación str:', np.std(arreglo))
print('percentil:', np.percentile(arreglo, 40))