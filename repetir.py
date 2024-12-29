string_qualquer = input("Digite qualquer string: ")
numero_repeticao= int(input("Digite o número de repetições: "))

resultado= " - " .join([string_qualquer] * numero_repeticao)

print(resultado)