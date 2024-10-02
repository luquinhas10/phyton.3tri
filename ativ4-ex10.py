numero = 12345  # Altere este valor para contar dígitos de outro número
contador = 0
while numero > 0:
    numero //= 10
    contador += 1
print(contador)
