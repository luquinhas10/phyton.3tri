def verificar_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "O número é divisível por 3 e 5."
    else:
        return "O número não é divisível por 3 e 5."

numero = int(input("Digite um número: "))
print(verificar_divisibilidade(numero))
