# SERIE A PARTIR DE UN DICCIONARIO
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
# Las llaves son los indices
print(serie)