# FUNCIONES UTILES DE CLASE
# -------------------------
class Cotorro:
    def __init__(self, nombre:str):
        self.nombre = nombre

class Perico:
    def __init__(self, nombre:str):
        self.nombre = nombre

pedro = Cotorro('Pedro')
pablo = Perico('Pablo')

# Conocer la clase de una instancia
print(isinstance(pedro, Perico))
print(isinstance(pedro, Cotorro))

# Detalles de una instancia
help(pedro)