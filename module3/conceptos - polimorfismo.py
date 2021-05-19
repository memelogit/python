# POLIMORFISMO
# ------------

class Animal:
    def __init__(self, nombre:str):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return self.sonido

class Perro(Animal):
    def __init__(self, nombre:str):
        super().__init__(nombre)
        self.sonido = 'Wof!'

class Gato(Animal):
    def __init__(self, nombre:str):
        super().__init__(nombre)
        self.sonido = 'Miauu!'

animales = [Perro('benji'), Gato('Tom')]
for animal in animales:
    print(animal.hacer_sonido())