vetor = [int(input(f"Digite o {i+1}º elemento do vetor: ")) for i in range(5)]
produto = 1
for num in vetor:
    produto *= num
print("Produto dos elementos do vetor:", produto)