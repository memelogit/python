# FILTRADO DE FILAS
# -----------------

import pandas as pd

df = pd.read_csv('https://corgis-edu.github.io/corgis/datasets/csv/video_games/video_games.csv')

# Juegos desde el 2006
print(df[df['Release.Year'] >= 2006])

# Juegos de Mario
print(df[df['Title'].str.contains('Mario')])