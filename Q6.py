# 6. Maior número até digitar 0
maior = None
while True:
    numero = float(input("Digite um número (0 para encerrar): "))
    if numero == 0:
        break
    if maior is None or numero > maior:
        maior = numero
print(f"Maior número: {maior}")