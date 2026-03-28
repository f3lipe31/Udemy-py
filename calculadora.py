while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite a operação (+, -,/): ")

    if operador == '+':
        resultado = num1 + num2
        print(f"O resultado é: {resultado}")
    elif operador == '-':
        resultado = num1 - num2
        print(f"O resultado é: {resultado}")
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
            continue
    else:
        print("Operação inválida.")
        continue

    sair = input("quer sair? [s]im: ").lower().startswith('s')
    if sair is True:
        break  
