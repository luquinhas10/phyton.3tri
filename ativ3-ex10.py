vetor = [int(input(f"Digite o {i+1}º elemento do vetor: ")) for i in range(5)]
ordenado = all(vetor[i] <= vetor[i + 1] for i in range(len(vetor) - 1))
if ordenado:
    print("O vetor está ordenado em ordem crescente.")
else:
    print("O vetor não está ordenado.")
