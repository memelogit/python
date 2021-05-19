# SERIES EN PANDAS
# ----------------

import pandas as pd

serie = pd.Series(
    data=[
        'Matemáticas',
        'Historia',
        'Economía',
        'Programación',
        'Inglés'
    ],
    dtype='string',
    index=[2,4,5,6,7] # opcional
)
print(serie)