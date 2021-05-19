# ATRIBUTOS DE UN DATAFRAME
# -------------------------

import pandas as pd

df = pd.read_csv('https://corgis-edu.github.io/corgis/datasets/csv/video_games/video_games.csv')

# Información general
print(df.info())

# Dimensión
print(df.shape)

# Número de elementos filas x columnas
print(df.size)

# Nombre de las columnas
print(df.columns)

# Nombre de las filas
print(df.index)

# Tipo de datos de las columnas
print(df.dtypes)

# Primeros 5 elementos
print(df.head(5))

# Ultimas 5 filas
print(df.tail(5))