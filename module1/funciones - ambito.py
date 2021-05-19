# AMBITO DE PARAMETROS
# --------------------

variable_global = 5

def imprime():
    variable_global = 3
    print('dentro:', variable_global)

imprime()
print('fuera', variable_global)