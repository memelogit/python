# SUB-CADENAS
# -----------

texto = 'Hola mundo'

# Extraemos 'Hola'
print(texto[0:4])  # hola
print(texto[:4])   # hola

# Extraemos 'mundo'
print(texto[5:10]) # mundo
print(texto[5:-1]) # mund
print(texto[5:])   # mundo

# Extraemos un mensaje extraño
print(texto[::2])  # Hl ud