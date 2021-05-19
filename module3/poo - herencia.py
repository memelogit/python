# HERENCIA
# --------

class Organismo:
    def __init__(self, vivo:bool=True):
        self.vivo = vivo

class Animal(Organismo):
    pass

class Planta(Organismo):
    pass

class Perro(Animal):
    def __init__(self, nombre:str):
        super().__init__(True)
        self.nombre = nombre
    
    def __str__(self):
        return f'nombre:{self.nombre} vivo:{self.vivo}'

class Gato(Animal):
    pass

benji = Perro('Benji')
print(benji)