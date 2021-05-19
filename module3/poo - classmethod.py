class Gato:

    mult_de_dosis = 0.003

    def __init__(self, nombre:str, peso:int):
        self.nombre = nombre
        self.peso = peso
    
    def vacunar(self):
        return 'suministramos {} litros contra la rinotraqueitis'.format(
            self.peso * Gato.mult_de_dosis
        )
    
    # La convención en métodos de clase es usar 'cls' en lugar de 'self'
    @classmethod
    def modificar_mult(cls, valor):
        cls.mult_de_dosis = valor

michi = Gato('Michi', 3.5)
print(michi.vacunar())
Gato.modificar_mult(0.006)
print(michi.vacunar())