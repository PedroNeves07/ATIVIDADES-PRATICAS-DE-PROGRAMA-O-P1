#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado

valor = input("Digite algo: ")

# Mostra o tipo original
print("Tipo original:", type(valor))

if:
    numero = float(valor)  # tenta converter para número
    print("É numérico!")
    print("Quadrado:", numero ** 2)
else:
    print("Não é um valor numérico.")







