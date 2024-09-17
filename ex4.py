def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return f"{ano} é um ano bissexto."
    else:
        return f"{ano} não é um ano bissexto."

ano = int(input("Digite um ano: "))
print(verificar_bissexto(ano))
