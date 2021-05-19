class Gato:

    def __init__(self, nombre):
        self.nombre = nombre
    
    # Método estático
    @staticmethod
    def hora_de_jugar(HH24) -> bool:
        if HH24 >= 8 and HH24 <= 20:
            return True
        else:
            return False

tom = Gato('Tom')
print(Gato.hora_de_jugar(12))