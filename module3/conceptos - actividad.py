# ACTIVIDAD
# ---------

# 1.- Construye la clase Punto que tome como argumentos de entrada
#     las posición en x,y. Después agrega el método coordenas_polares()
# 2.- Modifica el contructor de la clase Rectángulo para que acepte
#     puntos como argumentos de entrada
# 3.- Construye la clase Cuadrado que herede de la clase padre Rectángulo
#     Valida que los puntos correspondan con un cuadrado o muestra un
#     mensaje de error

import math

class Punto:
    def __init__(self, coords:tuple) -> None:
        self.x = coords[0]
        self.y = coords[1]
    
    def coordenas_polares(self) -> str:
        return f'r={math.sqrt(self.x**2 + self.y**2)} θ={math.atan(self.y/self.x)*180/math.pi}°'

class Rectangulo:

    def __init__(self, p1:tuple, p2:tuple):
        if p1[0] > p2[0]:
            self.base = p2[0] - p1[0]
        else:
            self.base = p1[0] - p2[0]
        
        if p1[1] > p2[1]:
            self.altura = p2[1] - p1[1]
        else:
            self.altura = p1[1] - p2[1]

    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2* self.base + 2 * self.altura
    
    def modificar_base(self, base:int) -> None:
        self.base = base

    def modificar_altura(self, altura:int) -> None:
        self.altura = altura

class Cuadrado(Rectangulo):

    def __init__(self, p1: tuple, p2: tuple):
        super().__init__(p1, p2)
        if self.base != self.altura:
            raise ValueError('Los puntos no corresponden a un cuadrado')

# Imprimimos las coordenadas polares del punto (12, 5)
p1 = Punto((12, 5))
print(p1.coordenas_polares())

# Creamo un rectángulo usando puntos
r = Rectangulo((5, 4), (1, 1))
print(r.area())

# Cuadrado válido
c = Cuadrado((1, 1), (2, 2))

# Cuadrado no válido, levanta una excepción
c = Cuadrado((5, 4), (1, 1))