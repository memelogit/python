# METODOS DE DICCIONARIOS
# -----------------------

glucosa = {
    'gaby': 100,
    'anita': 96,
    'pepe': 105,
    'carlos': 91,
    'isabela': 120
}

# Actualizar/añadir elementos
glucosa.update({
    'abraham': 103,
    'rosa': 95,
    'pepe': 108
})

# Eliminando elementos
glucosa.pop('rosa')
del glucosa['isabela']
print(glucosa)

# Limpiar diccionario
glucosa.clear()
print(glucosa)