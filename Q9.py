# 9. Contar positivos e negativos até digitar 0
positivos = 0
negativos = 0
while True:
    numero = float(input("Digite um número (0 para encerrar): "))
    if numero == 0:
        break
    if numero > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Positivos: {positivos} | Negativos: {negativos}")