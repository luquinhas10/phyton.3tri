def verificar_letra(letra):
    if letra.lower() in 'aeiou':
        return "A letra é uma vogal."
    else:
        return "A letra é uma consoante."

letra = input("Digite uma letra: ")
print(verificar_letra(letra))
