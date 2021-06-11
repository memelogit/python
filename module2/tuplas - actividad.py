# ACTIVIDAD
# ---------

# Escribir un programa que almacene las siguientes matrices 
# en tuplas y muestre en pantalla su producto

a = (
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9)
    )
b = (
        (1, -1, 2),
        (2, -1, 2),
        (3, -3, 0)
    )

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(a)):
   for j in range(len(b[0])):
       for k in range(len(b)):
           result[i][j] += a[i][k] * b[k][j]

for r in result:
   print(r)