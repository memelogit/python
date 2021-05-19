# ACCESO A ELEMENTOS DE UNA SERIE
# --------------------------------

import pandas as pd

serie = pd.Series(
    data={
        'Matemáticas': 7.2,
        'Historia': 8.4,
        'Economía': 6.9,
        'Programación': 10,
        'Inglés': 9.5
    }
)
# Por posición
print(serie[2:4])

# Por índices
print(serie[['Historia', 'Inglés']])