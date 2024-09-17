def verificar_intervalo(numero):
    if 10 <= numero <= 20:
        return "O número está entre 10 e 20."
    else:
        return "O número não está entre 10 e 20."

numero = float(input("Digite um número: "))
print(verificar_intervalo(numero))
