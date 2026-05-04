# 7. Média das notas até digitar -1
soma = 0
quantidade = 0
while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    soma += nota
    quantidade += 1
if quantidade > 0:
    print(f"Média: {soma / quantidade:.2f}")
else:
    print("Nenhuma nota informada.")