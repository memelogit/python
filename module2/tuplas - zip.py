# MÉTODO ZIP
# ----------

alumnos = ['hugo', 'paco', 'luis']
promedios = [10, 9, 10]
faltas = [3, 0, 1]

tupla = alumnos, promedios, faltas

for alumno, promedio, falta in zip(*tupla):
    print('alumno: {}, promedio: {}, faltas: {}'.format(
        alumno,
        promedio,
        falta
    ))