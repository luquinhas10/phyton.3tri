numero = 12345  # Altere este valor para outro número
soma_digitos = 0
while numero > 0:
    soma_digitos += numero % 10
    numero //= 10
print(soma_digitos)
