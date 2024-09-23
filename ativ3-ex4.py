vetor = [int(input(f"Digite o {i+1}º elemento do vetor: ")) for i in range(5)]
menor = vetor[0]
for num in vetor:
    if num < menor:
        menor = num
print("Menor elemento do vetor:", menor)
