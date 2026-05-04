# 5. Par ou ímpar até digitar 0
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")