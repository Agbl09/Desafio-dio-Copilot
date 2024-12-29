# Função para solicitar e validar a entrada de números
def solicitar_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

# Função para exibir um menu de operações
def exibir_menu():
    print("\nEscolha a operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Potência (**)")
    print("6 - Raiz quadrada (√)")
    print("7 - Sair")

# Função para realizar a operação
def realizar_operacao(opcao, num1, num2=None):
    if opcao == 1:
        return num1 + num2, "+"
    elif opcao == 2:
        return abs(num1 - num2), "-"
    elif opcao == 3:
        return num1 * num2, "*"
    elif opcao == 4:
        if num2 != 0:
            return num1 / num2, "/"
        else:
            return "Erro: divisão por zero não é permitida.", "/"
    elif opcao == 5:
        return num1 ** num2, "**"
    elif opcao == 6:
        if num1 >= 0:
            return num1 ** 0.5, "√"
        else:
            return "Erro: não é possível calcular a raiz quadrada de um número negativo.", "√"
    else:
        return None, "?"

# Programa principal
print("Bem-vindo ao programa de operações matemáticas avançadas!")

while True:
    exibir_menu()
    opcao = int(input("Digite o número da operação desejada: "))

    if opcao in [1, 2, 3, 4, 5]:
        num1 = solicitar_numero("Digite o 1° número: ")
        num2 = solicitar_numero("Digite o 2° número: ")
        resultado, simbolo = realizar_operacao(opcao, num1, num2)
    elif opcao == 6:
        num1 = solicitar_numero("Digite o 1° número: ")
        resultado, simbolo = realizar_operacao(opcao, num1)
    elif opcao == 7:
        print("Saindo do programa...")
        break
    else:
        resultado, simbolo = "Operação inválida.", "?"

    # Exibir o resultado
    if isinstance(resultado, (int, float)):
        print(f"O resultado de {num1} {simbolo} {num2 if opcao in [1, 2, 3, 4, 5] else ''} é: {resultado}")
    else:
        print(resultado)