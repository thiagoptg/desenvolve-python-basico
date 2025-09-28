#Q1 Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.

#Digite uma frase: Bom dia, meu nome é Davi.

#Frase salva em /Users/laranjeira/python-basico/frase.txt


import os

def main():
    frase = input("Digite uma frase: ")

    nome_arquivo = "frase.txt"

    # Abre o arquivo para escrita (cria se não existir)
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(frase)

    # Obtém o caminho absoluto do arquivo
    caminho_completo = os.path.abspath(nome_arquivo)

    print(f"Frase salva em {caminho_completo}")

if __name__ == "__main__":
    main()


#Q2 Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

#Bom

#dia

#meu

#nome

#é

#Davi

import os
import string

def main():
    arquivo_origem = "frase.txt"
    arquivo_destino = "palavras.txt"

    # Lê o conteúdo do arquivo original
    with open(arquivo_origem, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Remove caracteres não alfabéticos, mantendo letras acentuadas
    palavras = []
    for palavra in conteudo.split():
        palavra_limpa = "".join(c for c in palavra if c.isalpha())
        if palavra_limpa:  # evita strings vazias
            palavras.append(palavra_limpa)

    # Salva cada palavra em uma linha no novo arquivo
    with open(arquivo_destino, "w", encoding="utf-8") as f:
        for palavra in palavras:
            f.write(palavra + "\n")

    # Imprime o conteúdo do novo arquivo
    print("Conteúdo de 'palavras.txt':")
    with open(arquivo_destino, "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()


#Q3 Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". Em seguida crie um script em Python que abra o arquivo para leitura e imprima:
#O texto das primeiras 25 linhas
#O número de linhas do arquivo
#A linha com maior número de caracteres
#O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).


import re

# Abrir o arquivo para leitura
with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# 1. Imprimir as primeiras 25 linhas
print("🔹 Primeiras 25 linhas do roteiro:\n")
for linha in linhas[:25]:
    print(linha.strip())

# 2. Número de linhas do arquivo
num_linhas = len(linhas)
print(f"\n🔹 Número total de linhas: {num_linhas}")

# 3. Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print(f"\n🔹 Linha com maior número de caracteres:\n{linha_maior.strip()}")

# 4. Contagem de menções aos nomes "Nonato" e "Íria"
texto_completo = " ".join(linhas)

# Regex para encontrar "Nonato" e "Íria" com variações de maiúsculas/minúsculas
nonato_count = len(re.findall(r"\bnonato\b", texto_completo, re.IGNORECASE))
iria_count = len(re.findall(r"\bíria\b", texto_completo, re.IGNORECASE))

print(f"\n🔹 Menções ao personagem 'Nonato': {nonato_count}")
print(f"🔹 Menções ao personagem 'Íria': {iria_count}")

#Q4 Vamos fazer o jogo da forca! Antes de programar:
#Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
#Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.
#Escreva um programa em Python para executar o jogo, de acordo com as definições:
#Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
#Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
#No início exiba o número de letras na palavra como underscores;
#Permita que o jogador insira letras para adivinhar a palavra;
#Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
#Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
#Limite o número de tentativas para 6 (as partes do enforcado).
#gabarito_enforcado.txt

import random

# Função para imprimir o enforcado
def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Carregar palavras
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip().lower() for linha in f if linha.strip()]

# Escolher uma palavra aleatória
palavra = random.choice(palavras)
letras_descobertas = ["_" for _ in palavra]
letras_usadas = set()

# Carregar estágios do enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    estagios = conteudo.strip().split("=========\n")
    estagios = [estagio.strip() + "\n=========" for estagio in estagios]

# Jogo
erros = 0
MAX_ERROS = 6

print("🎯 Bem-vindo ao Jogo da Forca!")
print(f"A palavra tem {len(palavra)} letras: {' '.join(letras_descobertas)}")

while erros < MAX_ERROS and "_" in letras_descobertas:
    letra = input("\nDigite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("⚠️ Digite apenas uma letra válida.")
        continue

    if letra in letras_usadas:
        print("🔁 Você já tentou essa letra.")
        continue

    letras_usadas.add(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_descobertas[i] = letra
        print("✅ Letra correta!")
    else:
        erros += 1
        print("❌ Letra incorreta!")
        imprime_enforcado(erros, estagios)

    print(f"\nPalavra: {' '.join(letras_descobertas)}")
    print(f"Letras usadas: {', '.join(sorted(letras_usadas))}")
    print(f"Erros: {erros}/{MAX_ERROS}")

# Resultado final
if "_" not in letras_descobertas:
    print("\n🎉 Parabéns! Você acertou a palavra!")
else:
    print("\n💀 Você perdeu! A palavra era:", palavra)
    imprime_enforcado(MAX_ERROS, estagios)

 #Q5 A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.

#Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.

#No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.

#Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.

#A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.

#Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.


livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["A Revolução dos Bichos", "George Orwell", 1945, 152],
    ["Grande Sertão: Veredas", "João Guimarães Rosa", 1956, 624],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Capitães da Areia", "Jorge Amado", 1937, 288],
    ["Ensaio Sobre a Cegueira", "José Saramago", 1995, 312],
    ["O Nome da Rosa", "Umberto Eco", 1980, 512]
]

# Criar e escrever no arquivo CSV
with open("meus_livros.csv", "w", encoding="utf-8") as f:
    # Cabeçalho
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Dados dos livros
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        f.write(linha)

print("✅ Arquivo 'meus_livros.csv' criado com sucesso!")

#Q6 


import csv

def musica_top_por_ano(arquivo_csv):
    resultado = {}
    with open(arquivo_csv, "r", encoding="latin-1") as f:
        leitor = csv.DictReader(f)

        for linha in leitor:
            try:
                ano = int(linha["released_year"])
                if 2012 <= ano <= 2022:
                    nome = linha["track_name"]
                    artista = linha["artist(s)_name"]
                    streams = int(linha["streams"])

                    # verifica se já temos uma música para este ano
                    if ano not in resultado or streams > resultado[ano][3]:
                        resultado[ano] = [nome, artista, ano, streams]
            except ValueError:
                # ignora linhas com valores estranhos
                continue

    # organiza a saída em lista ordenada por ano
    lista_final = [resultado[ano] for ano in sorted(resultado.keys())]
    return lista_final


# Exemplo de uso:
arquivo = "spotify-2023.csv"
top10 = musica_top_por_ano(arquivo)
print(top10)
