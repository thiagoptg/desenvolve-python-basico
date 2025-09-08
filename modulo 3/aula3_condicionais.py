# lê as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# verifica se ambas são maiores de 17 anos
pode_entrar = (idade_juliana > 17) and (idade_cris > 17)

# imprime True ou False
print(pode_entrar)
#2 - Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris,
# mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário

# lê as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# verifica se pelo menos uma é maior de 17 anos
pode_entrar = (idade_juliana > 17) or (idade_cris > 17)

# imprime True ou False
print(pode_entrar)

#3 - Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro.
#  Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja e as impressões de seu código em branco.
# pergunta a idade
idade = int(input("Digite sua idade: "))

# pergunta se já jogou pelo menos 3 jogos (usuário digita True ou False)
jogou_3 = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")

# converte a string de entrada em valor booleano
jogou_3 = jogou_3.strip().lower() == "true"

# pergunta quantas vitórias teve
vitorias = int(input("Quantas vezes você venceu um jogo?: "))

# expressão de admissão: idade entre 16 e 18, já jogou >=3, e venceu >=1
pode_entrar = (16 <= idade <= 18) and jogou_3 and (vitorias >= 1)

# imprime True ou False
print(pode_entrar)

#4 - Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem.
#  Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:

#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.

#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.

#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

#O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida. Segue um exemplo de interação com seu código no terminal, com entradas de dados 
# destacadas em laranja e as impressões de seu código em branco.
# lê a classe escolhida
classe = input("Digite a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()

# lê os pontos de atributos
forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

# verifica consistência conforme a classe
if classe == "guerreiro":
    valido = (forca >= 15) and (magia <= 10)
elif classe == "mago":
    valido = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro":
    valido = (forca > 5 and forca <= 15) and (magia > 5 and magia <= 15)
else:
    # classe inválida
    valido = False

# imprime True ou False
print(valido)


#5 - Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.

#B: Ou ter trabalhado pelo menos 30 anos

#C: Ou ter 60 anos  e trabalhado pelo menos 25.

# lê os dados do usuário
genero = input("Digite seu gênero (M/F): ").strip().upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

# regras de aposentadoria
# A: mulheres > 60 ou homens > 65
regra_a = (genero == "F" and idade > 60) or (genero == "M" and idade > 65)

# B: trabalhou pelo menos 30 anos
regra_b = tempo_servico >= 30

# C: 60 anos e trabalhou pelo menos 25
regra_c = (idade == 60 and tempo_servico >= 25)

# expressão final
aposentar = regra_a or regra_b or regra_c

# imprime True ou False
print(aposentar)

