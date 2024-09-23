vetor = [int(input(f"Digite o {i+1}º elemento do vetor: ")) for i in range(5)]
maior = max(vetor)
menor = min(vetor)
diferenca = maior - menor
print("Diferença entre maior e menor valor:", diferenca)
