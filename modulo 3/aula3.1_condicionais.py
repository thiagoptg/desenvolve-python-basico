# lê os dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# calcula a soma
soma = num1 + num2

# verifica se a soma é par ou ímpar
if soma % 2 == 0:
    print("Par")
else:
    print("Ímpar")
#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5.
#  O programa deve imprimir uma mensagem correspondente à classificação do filme:
# lê a avaliação do usuário (1 a 5)
avaliacao = int(input("Digite a avaliação do filme (1 a 5): "))

# verifica a classificação correspondente
if avaliacao == 5:
    print("Excelente")
elif avaliacao == 4:
    print("Muito bom")
elif avaliacao == 3:
    print("Bom")
elif avaliacao == 2:
    print("Regular")
elif avaliacao == 1:
    print("Ruim")
else:
    print("Avaliação inválida")
#Você está desenvolvendo um programa para verificar se um ano é bissexto. 
# Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto". 

#Teste seu código com os valores: 1900 (não bissexto), 
# 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 
# lê o ano
ano = int(input("Digite um ano: "))

# verifica se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")
#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
# lê a distância da entrega (km)
distancia = float(input("Digite a distância da entrega (km): "))

# lê o peso do pacote (kg)
peso = float(input("Digite o peso do pacote (kg): "))

# define o valor por kg conforme a distância
if distancia <= 100:
    valor_kg = 1.0
elif distancia <= 300:
    valor_kg = 1.5
else:
    valor_kg = 2.0

# calcula o frete base
frete = valor_kg * peso

# acrescenta taxa de 10 reais se peso > 10kg
if peso > 10:
    frete += 10

# imprime o valor do frete
print(f"Valor do frete: R${frete:.2f}")
