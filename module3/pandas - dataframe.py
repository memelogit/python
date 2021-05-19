# DATAFRAME
# ---------

import pandas as pd

# DataFrame a partir de un diccionario
datos = {
    'nombre': ['María', 'Luis', 'Carmen', 'Antonio'],
    'edad': [18, 22, 20, 21],
    'grado': ['Economía', 'Medicina', 'Arquitectura', 'Economía'],
    'correo': ['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}
df = pd.DataFrame(datos)
print(df)

# DataFrame a partir de una lista de listas
df = pd.DataFrame(
    data = [
        ['María', 18],
        ['Luis', 22],
        ['Carmen', 20]
    ],
    columns=['Nombre', 'Edad']
)
print(df)