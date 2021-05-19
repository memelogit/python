# ARGUMENTOS POR DEFECTO
# ----------------------

def expediente(nombre:str, curso:str='Propedéutico') -> str:
    return f'El alumno {nombre} inscrito en {curso}'

# Argumentos posicionales
print(expediente('Aldo'))

# Argumentos nominales
print(expediente(curso='Matemáticas', nombre='Aldo'))