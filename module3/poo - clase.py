# CLASE
# -----

class Clase:

    # Constructor
    def __init__(self, argumento:int):
        self.argumento = argumento
    
    # Método
    def metodo(self):
        return self.argumento

instancia = Clase(argumento=3)
print(instancia.metodo())