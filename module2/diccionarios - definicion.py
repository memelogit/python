# DICCIONARIOS
# ------------

diccionario = {
    'nombre': 'Juan',
    'edad': 48,
    'peso': 61.63,
    'soltero': True,
    'domicilio': {
        'ciudad': 'Guadalajara',
        'c.p.': 45200
    }
}

# Acceso a elementos
print(f'El nombre es: {diccionario["nombre"]}')
print(f'C.P.: {diccionario["domicilio"]["c.p."]}')

# Mofificacion de elementos
diccionario['edad'] += 1
print(diccionario)