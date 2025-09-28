##Q1 Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.

#Digite seu nome: Fulano

#F

#Fu

#Ful

#Fula

#Fulan

#Fulano
def main():
    nome = input("Digite seu nome: ")

    for i in range(1, len(nome)+1):
        print(nome[:i])


if __name__ == "__main__":
    main()


#Q2 Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

#Digite seu primeiro nome: Alice

#Digite seu sobrenome: Silva

#Bem-vinda, Alice Silva! 

 
def main():
    primeiro_nome = input("Digite seu primeiro nome: ")
    sobrenome = input("Digite seu sobrenome: ")

    nome_completo = primeiro_nome + " " + sobrenome

    print(f"Bem-vinda, {nome_completo}!")


if __name__ == "__main__":
    main()

#Q3 Escreva um script que dado uma frase conta os espaços em branco.

#Digite a frase: Meu amor mora em Roma e me deu um ramo de flores

#Espaços em branco: 11

 
def main():
    frase = input("Digite a frase: ")

    espacos = frase.count(" ")

    print(f"Espaços em branco: {espacos}")


if __name__ == "__main__":
    main()

#Q4 Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.

#Digite o número: 97651234

#Número completo: 99765-1234

#Digite o número: 980876543

#Número completo: 98087-6543 
def main():
    numero = input("Digite o número: ")

    # Remove espaços ou traços caso o usuário tenha digitado
    numero = numero.replace(" ", "").replace("-", "")

    if len(numero) == 8:
        # Acrescenta 9 na frente
        numero = "9" + numero
    elif len(numero) == 9:
        # Se já tiver 9 dígitos, verifica se começa com 9
        if numero[0] != "9":
            print("Número inválido: deve começar com 9.")
            return
    else:
        print("Número inválido: deve ter 8 ou 9 dígitos.")
        return

    # Adiciona o separador "-"
    numero_formatado = numero[:5] + "-" + numero[5:]

    print(f"Número completo: {numero_formatado}")


if __name__ == "__main__":
    main()

#Q5 Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:

#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores

#19 vogais

#Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]
def main():
    frase = input("Digite uma frase: ")

    # Lista de índices onde a letra é vogal
    indices_vogais = [i for i, letra in enumerate(frase.lower()) if letra in "aeiou"]

    print(f"{len(indices_vogais)} vogais")
    print(f"Índices {indices_vogais}")


if __name__ == "__main__":
    main()

#Q6 Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores

#Digite a palavra objetivo: amor

#Anagramas: ["amor", "mora", "ramo", "Roma"] 
def main():
    frase = input("Digite uma frase: ")
    palavra_objetivo = input("Digite a palavra objetivo: ")

    # Normaliza a palavra objetivo para letras minúsculas e ordena
    palavra_sorted = sorted(palavra_objetivo.lower())

    # Lista de palavras da frase
    palavras = frase.split()

    # Encontra anagramas
    anagramas = [palavra for palavra in palavras if sorted(palavra.lower()) == palavra_sorted]

    print("Anagramas:", anagramas)


if __name__ == "__main__":
    main()

#Q7 Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

#Chave de criptografia: gere um valor n aleatório entre 1 e 10

#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

#nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

#chave_aleatoria = 5

#nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']
import random

def encrypt(nomes):
    """
    Recebe uma lista de strings e retorna:
    - lista de nomes criptografados
    - chave de criptografia (número aleatório entre 1 e 10)
    """
    # Gera chave aleatória entre 1 e 10
    chave = random.randint(1, 10)

    nomes_cript = []

    for nome in nomes:
        cript = ""
        for c in nome:
            if 33 <= ord(c) <= 126:
                # desloca o caractere, respeitando o intervalo 33-126
                novo = 33 + (ord(c) - 33 + chave) % (126 - 33 + 1)
                cript += chr(novo)
            else:
                # se não estiver no intervalo, mantém o caractere
                cript += c
        nomes_cript.append(cript)

    return nomes_cript, chave


def main():
    nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

    nomes_cript, chave = encrypt(nomes)

    print("Chave de criptografia:", chave)
    print("Nomes criptografados:", nomes_cript)


if __name__ == "__main__":
    main()

#Q8 Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 

def calcula_digito(cpf_parcial):
    """
    Recebe uma string de 9 ou 10 dígitos e calcula o próximo dígito verificador
    """
    tamanho = len(cpf_parcial)
    if tamanho == 9:
        multiplicadores = list(range(10, 1, -1))
    elif tamanho == 10:
        multiplicadores = list(range(11, 1, -1))
    else:
        raise ValueError("CPF parcial deve ter 9 ou 10 dígitos")
    
    total = sum(int(d) * m for d, m in zip(cpf_parcial, multiplicadores))
    resto = total % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)


def validar_cpf(cpf):
    """
    Valida o CPF no formato XXX.XXX.XXX-XX
    """
    # Remove pontos e traço
    cpf_numeros = cpf.replace('.', '').replace('-', '')

    # Deve ter 11 dígitos
    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
        return False

    # Primeiro dígito verificador
    digito1 = calcula_digito(cpf_numeros[:9])

    # Segundo dígito verificador
    digito2 = calcula_digito(cpf_numeros[:9] + digito1)

    # Verifica se os dígitos calculados são iguais aos informados
    return cpf_numeros[-2:] == digito1 + digito2


def main():
    cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

    if validar_cpf(cpf_usuario):
        print("Válido")
    else:
        print("Inválido")


if __name__ == "__main__":
    main()


 