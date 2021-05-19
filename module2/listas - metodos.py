# METODOS DE LISTAS
# -------------------

lista = [1, 2, 2, 3, 4]
lista.append(2)
print('total numero 2:', lista.count(2))

lista.extend([5, 6])
print('indice de 5:', lista.index(5))

# Insertar el elemento 9 en la posicion 6
lista.insert(6, 9)
print(lista)

# Removemos elementos de la lista
lista.pop(-1)
lista.remove(2)
print('eliminamos elementos:', lista)

# Manipulacion
lista.reverse()
lista.sort()
print('manipulacion', lista)
