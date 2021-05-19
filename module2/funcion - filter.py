# FUNCION FILTER
# --------------

def multiple(numero):
    if numero % 5 == 0:
        return True

numeros = [2, 5, 10, 23, 50, 33]

print(list(filter(multiple, numeros)))