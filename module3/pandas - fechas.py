# MANEJO DE FECHAS
# ----------------

import pandas as pd
from datetime import datetime

covid_df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
print(covid_df['date'])

# Convertir la columna 'date' del tipo object al tipo 'datetime'
# Usando el metodo .to_datetime()
covid_df['date'] = pd.to_datetime(
    covid_df['date'],
    format='%Y-%m-%d'
)

# Usando el metodo .apply()
covid_df['date'] = covid_df['date'].apply(
    lambda celda: datetime.strptime(celda,'%Y-%m-%d')
)

# Usando el metodo .astype()
covid_df['date'] = covid_df['date'].astype('datetime64[ns]', '%Y-%m-%d')
print(covid_df['date'])