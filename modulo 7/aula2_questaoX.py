#Q1 Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa fazer um "if" para cada mês.

#Digite uma data de nascimento: 29/10/1973

#Você nasceu em  29 de Outubro de 1973.
def main():
    # Lista com os nomes dos meses
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    data = input("Digite a data de nascimento (dd/mm/aaaa): ")

    # Divide a string em dia, mês e ano
    try:
        dia, mes, ano = data.split("/")
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if 1 <= mes <= 12:
            print(f"Você nasceu em {dia} de {meses[mes-1]} de {ano}.")
        else:
            print("Mês inválido.")
    except ValueError:
        print("Data inválida. Use o formato dd/mm/aaaa.")


if __name__ == "__main__":
    main()

#Q2 Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

#Digite uma frase: O rato roeu a roupa do rei

#Frase modificada: * r*t* r*** * r**p* d* r**
def main():
    frase = input("Digite uma frase: ")

    vogais = "aeiouAEIOU"

    frase_modificada = "".join(["*" if letra in vogais else letra for letra in frase])

    print("Frase modificada:", frase_modificada)


if __name__ == "__main__":
    main()

#Q3 Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".

#Digite uma frase (digite "fim" para encerrar): Radar

#"Radar" é palíndromo

#Digite uma frase (digite "fim" para encerrar): Bom dia!

#"Bom dia!" não é palíndromo

#Digite uma frase (digite "fim" para encerrar): Ame o poema

#"Ame o poema" é palíndromo

#Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!

#"A Daniela ama a lei? Nada!" é palíndromo
import string

def limpar_texto(texto):
    """
    Remove espaços e pontuação, e transforma em minúsculas.
    """
    return "".join(c.lower() for c in texto if c.isalnum())

def main():
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
        if frase.lower() == "fim":
            break
        
        frase_limpa = limpar_texto(frase)
        if frase_limpa == frase_limpa[::-1]:
            print(f'"{frase}" é palíndromo\n')
        else:
            print(f'"{frase}" não é palíndromo\n')

if __name__ == "__main__":
    main()



#Q4 Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:

#Pelo menos 8 caracteres de comprimento.

#Contém pelo menos uma letra maiúscula e uma letra minúscula.

#Contém pelo menos um número.

#Contém pelo menos um caractere especial (por exemplo, @, #, $).

#def validador_senha(senha):

    #### Escreva a função


# Exemplo de uso:

#senha1 = "Senha123@"

#senha2 = "senhafraca"

#senha3 = "Senha_fraca"

#print(validador_senha(senha1))  # Saída esperada: True

#print(validador_senha(senha2))  # Saída esperada: False

#print(validador_senha(senha3))  # Saída esperada: False

import string

def validador_senha(senha):
    """
    Retorna True se a senha atender aos critérios:
    - Pelo menos 8 caracteres
    - Pelo menos uma letra maiúscula e uma minúscula
    - Pelo menos um número
    - Pelo menos um caractere especial
    """
    if len(senha) < 8:
        return False

    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(c in string.punctuation for c in senha)

    return all([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])


# Exemplo de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # True
print(validador_senha(senha2))  # False
print(validador_senha(senha3))  # False

#Q5 Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
#Dica: use a biblioteca random.

#def embaralhar_palavras(frase):

    #### Escreva a função


# Exemplo de uso:

#frase = "Python é uma linguagem de programação"

#resultado = embaralhar_palavras(frase)

#
# print(resultado)

# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

 



import random

def embaralhar_palavras(frase):
    """
    Recebe uma frase e retorna uma nova frase com as letras internas de cada palavra embaralhadas.
    Mantém o primeiro e último caractere da palavra no lugar.
    """
    palavras = frase.split()
    frase_embaralhada = []

    for palavra in palavras:
        if len(palavra) > 3:  # Apenas palavras com mais de 3 letras podem ser embaralhadas internamente
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = palavra[0] + "".join(meio) + palavra[-1]
        else:
            nova_palavra = palavra  # Palavras pequenas permanecem iguais
        frase_embaralhada.append(nova_palavra)

    return " ".join(frase_embaralhada)





 