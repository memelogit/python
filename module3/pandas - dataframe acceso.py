# ACCESO A UN DATAFRAME
# ---------------------

import pandas as pd

df = pd.read_csv('https://corgis-edu.github.io/corgis/datasets/csv/video_games/video_games.csv')

# Acceso a través de fila, columna
print(df.iloc[0, 0])

# Acceso a través de rangos
print(df.iloc[0:3, 0:5])

# Acceso a través de nombres de columnas
print(df[['Title', 'Release.Year']])