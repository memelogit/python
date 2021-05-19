# LECTURA DESDE FICHERO
# ---------------------

import pandas as pd

# Importamos desde un CSV
df = pd.read_csv(
    'https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv',
    sep=','
)
print(df)

# Exportamos a Excel
df.to_excel('pandas.xlsx')