
def main():
    # 1) Números pares entre 20 e 50
    pares = [n for n in range(20, 51) if n % 2 == 0]

    # 2) Quadrados de 1 a 9
    quadrados = [n**2 for n in [1,2,3,4,5,6,7,8,9]]

    # 3) Números divisíveis por 7 entre 1 e 100
    divisiveis_7 = [n for n in range(1, 101) if n % 7 == 0]

    # 4) "par" ou "ímpar" para range(0,30,3)
    paridade = ["par" if n % 2 == 0 else "ímpar" for n in range(0, 30, 3)]

    # Mostrando os resultados
    print("Pares entre 20 e 50:", pares)
    print("Quadrados de 1 a 9:", quadrados)
    print("Divisíveis por 7 até 100:", divisiveis_7)
    print("Paridade em range(0,30,3):", paridade)


if __name__ == "__main__":
    main()
