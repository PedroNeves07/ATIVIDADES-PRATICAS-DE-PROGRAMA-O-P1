# 10. Adivinhe o número
NUMERO_SECRETO = 42
while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite == NUMERO_SECRETO:
        print("Acertou!")
        break
    elif palpite < NUMERO_SECRETO:
        print("Muito baixo! Tente maior.")
    else:
        print("Muito alto! Tente menor.")