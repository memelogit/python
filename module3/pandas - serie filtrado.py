# FILTRADO DE SERIES
# ------------------

import pandas as pd

serie = pd.Series({
    'Matemáticas': 6.0,
    'Economía': 4.5,
    'Programación': 8.5
})

print(serie[serie > 5])