# PRIMEIRO FLUXOGRAMA
# Lê o valor de x
x = int(input("Digite um valor para x: "))

# Verifica se x é maior que 5
if x > 5:
    print("Maior que 5")

# Imprime "Fim" independentemente da condição
print("Fim")
#SEGUNDO FLUXOGRAMA
# Lê o valor de n
n = int(input("Digite um valor para n: "))

# Inicializa o contador
cont = 0

# Enquanto cont for menor ou igual a n
while cont <= n:
    cont += 1
    print(cont)

# Imprime "Fim" ao final do processo
print("Fim")
#TERCEIRO FLUXOGRAMA
# Lê as três notas
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

# Calcula a média
m = (n1 + n2 + n3) / 3

# Verifica a situação do aluno
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

# Imprime "Fim" ao final
print("Fim")
#QUARTO FLUXOGRAMA
# Lê a quantidade de números que serão comparados
n = int(input("Quantos números você vai digitar? "))

# Inicializa a variável 'maior' com 0
maior = 0

# Executa o laço enquanto houver números a serem lidos
while n > 0:
    x = float(input("Digite um número: "))
    
    # Verifica se o número atual é maior que o maior até agora
    if x > maior:
        maior = x
    
    # Decrementa o contador
    n -= 1

# Imprime o maior valor encontrado
print("Maior:", maior)
print("Fim")
#EXERCíCIO 5
# Lê a quantidade de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Inicializa a soma das idades
soma_idades = 0

# Lê as idades e acumula a soma
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i + 1}: "))
    soma_idades += idade

# Calcula a média
media = soma_idades / N

# Imprime a média com duas casas decimais
print(f"Média das idades: {media:.2f}")
#EXERCÌCIO 6
# Lê a quantidade de experimentos
N = int(input("Digite a quantidade de experimentos: "))

# Inicializa os contadores
total = 0
sapos = 0
ratos = 0
coelhos = 0

# Processa cada experimento
for _ in range(N):
    entrada = input("Digite a quantidade e o tipo (ex: 10 C): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1].upper()

    total += quantia

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

# Calcula os percentuais
percentual_coelhos = (coelhos / total) * 100
percentual_ratos = (ratos / total) * 100
percentual_sapos = (sapos / total) * 100

# Exibe os resultados
print(f"\nTotal de cobaias: {total}")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")

print(f"\nPercentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")