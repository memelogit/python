# ACTIVIDAD
# ---------

# Construye la clase Rectángulo la cual tome como argumentos del
# constructor: base y altura. A demás implementa los siguientes métodos:
# - area()
# - perimetro()
# - modificar_base(base)
# - modificar_altura(altura)

class Rectangulo:

    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2* self.base + 2 * self.altura
    
    def modificar_base(self, base:int) -> None:
        self.base = base

    def modificar_altura(self, altura:int) -> None:
        self.altura = altura

r = Rectangulo(base=3, altura=4)
r.modificar_altura(altura=5)
r.modificar_base(base=4)
print('área:', r.area())
print('perímetro:', r.perimetro())