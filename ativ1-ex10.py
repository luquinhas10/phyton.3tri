num = int(input("Digite um número: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print("Fatorial de", num, "é:", fatorial)
