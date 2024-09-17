def verificar_maior(a, b):
    if a > b:
        return f"{a} é maior que {b}."
    elif b > a:
        return f"{b} é maior que {a}."
    else:
        return "Os dois números são iguais."

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print(verificar_maior(a, b))
