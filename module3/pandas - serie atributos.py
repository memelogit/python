# ATRIBUTOS DE SERIES
# -------------------

import pandas as pd

# Las llaves son los indices
serie = pd.Series(
    data={
        'Matemáticas': 7.2,
        'Historia': 8.4,
        'Economía': 6.9,
        'Programación': 10,
        'Inglés': 9.5
    }
)
print('tamaño:', serie.size)
print('lista:', serie.index)
print('tipo:', serie.dtype)