# APLICAR FUNCIONES A SERIES
# --------------------------

import pandas as pd
import math

serie = pd.Series([1, 2, 3, 4])
serie = serie.apply(math.log)
print(serie)

serie = pd.Series(['hugo', 'paco', 'luis'])
print(serie.apply(str.capitalize))