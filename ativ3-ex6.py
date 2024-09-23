vetor = [int(input(f"Digite o {i+1}º elemento do vetor: ")) for i in range(5)]
contagem_pares = sum(1 for num in vetor if num % 2 == 0)
print("Número de elementos pares:", contagem_pares)
