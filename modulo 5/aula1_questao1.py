# lê os dois números decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# calcula a diferença absoluta e arredonda para 2 casas
diferenca = round(abs(num1 - num2), 2)

# exibe o resultado
print(f"A diferença absoluta entre os números é: {diferenca}")
