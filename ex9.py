def classificar_nota(nota):
    if nota >= 7:
        return "Aprovado."
    elif 5 <= nota < 7:
        return "Recuperação."
    else:
        return "Reprovado."

nota = float(input("Digite a nota (0 a 10): "))
print(classificar_nota(nota))
