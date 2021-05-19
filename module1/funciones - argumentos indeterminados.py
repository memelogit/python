# ARGUMENTOS INDETERMINADOS
# -------------------------

def fiesta(*personas, lugar='ITESO') -> None:
    print(f'Invitados al {lugar}', end=': ')
    for persona in personas:
        print(persona, end=', ')

fiesta('Hugo', 'Paco', 'Luis')