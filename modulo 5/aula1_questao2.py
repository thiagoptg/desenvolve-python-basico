import random
import math

# lê o valor de n
n = int(input("Digite a quantidade de valores aleatórios: "))

soma = 0

# gera n valores aleatórios entre 0 e 100 e acumula a soma
for i in range(n):
    valor = random.randint(0, 100)
    soma += valor
    print(f"Valor {i+1}: {valor}")

# calcula a raiz quadrada da soma
raiz = math.sqrt(soma)

# mostra os resultados
print(f"\nSoma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz:.2f}")
