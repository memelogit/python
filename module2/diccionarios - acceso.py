# ACCESO SEGURO
# -------------

peliculas = {
    'totoro': 98,
    'death note': 91,
    'viaje de chijiro': 96,
    'coraline': 95
}

# Error al tratar de acceder al elemento
print(peliculas['inception'])

# Preguntamos antes de acceder
if 'totoro' in peliculas:
    print(peliculas['totoro'])

if 'death note' in peliculas.keys():
    print(peliculas['death note'])

if peliculas.get('coraline'):
    print(peliculas['coraline'])

if peliculas.get('inception'):
    print(peliculas['inception'])
else:
    print('-E- No se encontró la película')