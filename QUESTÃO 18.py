#Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou
#neutro.

a = float(input("DIGA UM NUMERO:"))
b = float(input("DIGA OUTRO:"))

if ( a == b):
    print("SÃO IGUAIS")

elif ( a > b):
    print(a, "É MAIOR QUE", b, "POR ISSO SAO DIFERENTES")

elif (b > a):
    print(b, "É MAIOR QUE", a, "POR ISSO SAO DIFERENTES")           


