# ACTIVIDAD
# ---------

# 1.- Escribir una función que reciba un objeto tipo Lista
# con números enteros aleatorios y retorne otra lista con
# sus cuadrados

def cuadrado(lista_referencia:list) -> list:
    '''
    Retorna el cuadrado de numeros alojados en una lista
    '''
    lista = []
    for i in lista_referencia:
        lista.append(i**2)
    return lista

print(cuadrado([1, 2, 3, 4, 5]))

# 2.- Escribir una función que convierta un número decimal
# en binario y otra que convierta un número binario en decimal

def to_decimal(binario:str) -> int:
    '''Retorna el número decimal correspondiente a 'binario'.
    '''
    binario = list(binario)
    binario.reverse()
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2 ** i
    return decimal

def to_binary(decimal:int) -> str:
    '''Retorna el número binario correspondiente a 'decimal'.
    '''
    binary = []
    while decimal > 0:
        binary.append(str(decimal % 2))
        decimal //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))