def calculadora():
    while True:
        print("\nEscolha a operação desejada:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        try:
            escolha = int(input("Digite o número da operação: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue

        if escolha == 0:
            print("Saindo da calculadora...")
            break
        elif escolha not in [1, 2, 3, 4]:
            print("Essa opção não existe.")
            continue

        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Valores inválidos. Digite números.")
            continue

        if escolha == 1:
            resultado = num1 + num2
        elif escolha == 2:
            resultado = num1 - num2
        elif escolha == 3:
            resultado = num1 * num2
        elif escolha == 4:
            if num2 == 0:
                print("Erro: Divisão por zero.")
                continue
            resultado = num1 / num2

        print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()
