# ACTIVIDAD
# ---------

# Dada la siguiente lista anidada. Accede a los elementos mencionados
# 1.- pera
# 2.- habanero
# 3.- pozole
# 4.- [limón, pepino]
# 5.- [habanero, árbol]
# 6.- Último elemento de la colección de frutas
# 7.- Último elemento de la colección de chiles
# 8.- Modifica el elemento pepino por [calabaza, zanahoria]

lista = [
    [
        ['naranja', 'pera', 'manzana'],
        'limón',
        'pepino',
        ['habanero', 'arbol']
    ],
    'enchiladas',
    'pozole'
]

# 1.- pera
print(lista[0][0][1])

# 2.- habanero
print(lista[0][3][0])

# 3.- pozole
print(lista[2])

# 4.- [limón, pepino]
print(lista[0][1:3])

# 5.- [habanero, árbol]
print(lista[0][3])

# 6.- Último elemento de la colección de frutas
print(lista[0][0][-1])

# 7.- Último elemento de la colección de chiles
print(lista[0][3][-1])

# 8.- Modifica el elemento pepino por [calabaza, zanahoria]
lista[0][2] = ['calabaza','zanahoria']
print(lista)