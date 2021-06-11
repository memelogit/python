# ACTIVIDAD
# ---------

# Escribir un programa que pregunte al usuario la fecha de su
# nacimiento en formato dd/mm/aaaa y muestra por pantalla, el
# día, el mes y el año. Tu programa también debe funcionar 
# cuando el día o el mes se introduzcan con un solo carácter

fecha = input('Introduce la fecha de tu nacimiento en formato día/mes/año: ')
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]

print('Día', dia)
print('Mes', mes)
print('Año', año)