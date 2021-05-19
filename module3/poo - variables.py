# VARIABLES DE CLASE E INSTANCIA
# ------------------------------

class Perro:

    tipo = 'canino'  # Variable de clase

    def __init__(self, nombre:str):
        self.nombre = nombre  # Variable de instancia

benji = Perro('benji')
tomas = Perro('tomás')

print(benji.nombre, benji.tipo)
print(tomas.nombre, tomas.tipo)