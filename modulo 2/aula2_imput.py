#Q1
# lê o comprimento (m) como inteiro
comprimento = int(input("Digite o comprimento do terreno (m): "))

# lê a largura (m) como inteiro
largura = int(input("Digite a largura do terreno (m): "))

# lê o preço por metro quadrado (R$) como ponto flutuante
preco= float(input("Digite o preço do metro quadrado R$: "))

# calcula a área do terreno 
area= comprimento * largura

# calcula o preço total do terreno
preco_total = preco * area

# imprime o resultado formatado
print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f})

#Q2
# lê um valor inteiro em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# converte para Celsius usando a fórmula e já transforma em inteiro
celsius = int((fahrenheit - 32) * (5/9))

# imprime a mensagem formatada
print(fahrenheit ,"graus Fahrenheit são ",celsius, "graus Celsius")

#Q3
# produto 1
nome1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
qtd1 = int(input("Digite a quantidade do produto 1: "))

# produto 2
nome2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
qtd2 = int(input("Digite a quantidade do produto 2: "))

# produto 3
nome3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
qtd3 = int(input("Digite a quantidade do produto 3: "))

# cálculo do total
total = (preco1 * qtd1) + (preco2 * qtd2) + (preco3 * qtd3)

# impressão com separador de milhar e duas casas decimais
print("Total: R$",total)

#Q4

# lê a quantia em reais (valor inteiro)
valor = int(input())

# calcula a quantidade de cada nota
notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20

notas10 = valor // 10
valor %= 10

notas5 = valor // 5
valor %= 5

notas2 = valor // 2
valor %= 2

notas1 = valor // 1

# impressão
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")


