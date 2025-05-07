def calculadora():
    print("Calculadora Simples")
    print("Operações disponíveis:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    while True:
        try:
            operacao = int(input("\nDigite o número da operação desejada: "))
            
            if operacao == 0:
                print("Encerrando a calculadora...")
                break
            elif operacao not in [1, 2, 3, 4]:
                print("Opção inválida! Por favor, escolha uma operação válida.")
                continue
                
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == 1:
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacao == 2:
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacao == 3:
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacao == 4:
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                    
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")


calculadora()