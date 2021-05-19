# ITERANDO DICCIONARIOS
# ---------------------

alumnos = {
    'Antonio': 8.9,
    'Paco': 9.5,
    'Hugo': 10,
    'Luis': 9.3
}

# Iterando sobre llave-valor
for nombre, calificacion in alumnos.items():
    print(nombre, calificacion)

# Iterando sobre llaves
for nombre in alumnos.keys():
    print(nombre)

# Iterando sobre valores
for calificacion in alumnos.values():
    print(calificacion)