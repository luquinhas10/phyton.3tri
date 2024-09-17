def verificar_signo(numero):
    if numero > 0:
        return "O número é positivo."
    elif numero < 0:
        return "O número é negativo."
    else:
        return "O número é zero."

numero = float(input("Digite um número: "))
print(verificar_signo(numero))
