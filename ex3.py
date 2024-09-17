def verificar_idade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

idade = int(input("Digite sua idade: "))
print(verificar_idade(idade))

