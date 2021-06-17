# ACTIVIDAD
# ---------

import pandas as pd

covid_df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

# Filtrado por ubicacion
covid_df = covid_df[covid_df.location == 'Mexico']

# Filtrado por fecha
covid_df['date'] = covid_df['date'].astype('datetime64[ns]')
covid_df = covid_df[covid_df.date == pd.Timestamp(2021, 5, 18)]

# Imprimir paciente hospitalizados
print(covid_df[['location', 'date', 'total_cases']])