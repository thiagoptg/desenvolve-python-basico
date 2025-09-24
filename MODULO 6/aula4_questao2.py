def main():
    frase = input("Digite uma frase: ")

    # Definindo vogais
    vogais_set = "aeiouAEIOU"

    # Lista de vogais (mantém repetição, ordena no final)
    vogais = sorted([ch for ch in frase if ch in vogais_set])

    # Lista de consoantes (ignora espaços)
    consoantes = [ch for ch in frase if ch.isalpha() and ch not in vogais_set]

    print("Vogais:", vogais)
    print("Consoantes:", consoantes)


if __name__ == "__main__":
    main()
