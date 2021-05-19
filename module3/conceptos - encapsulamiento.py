# ENCAPSULAMIENTO
# ---------------

class Avion:
    def __init__(self, id:str):
        self.id = id
        # Simulamos atributos privados
        self.__velocidad = 0
        self.__altitud = 0
        self.__roll = 0
        self.__pitch = 0
        self.__yaw = 0
    
    def volar(self):
        return f'volando...'

volaris555 = Avion('Volaris 555')