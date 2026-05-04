while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            break
        print("Valor fora do intervalo! Digite entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número.")

print(f"Nota aceita: {nota}")