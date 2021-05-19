# TIPOS DE ARGUMENTOS
# -------------------

def expediente(nombre:str, curso:str) -> str:
    return f'El alumno {nombre} inscrito en {curso}'

# Argumentos posicionales
print(expediente('Aldo', 'Propedéutico'))

# Argumentos nominales
print(expediente(curso='Propedéutico', nombre='Aldo'))