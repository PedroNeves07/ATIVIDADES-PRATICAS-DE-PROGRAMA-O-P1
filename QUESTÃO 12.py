#Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais

n1 = float(input("INFORME UM NUMERO:"))
n2 = float(input("DIGA OUTRO:"))
s = n1 + n2 

print ("A SOMA É:", s)

if ( n1 > n2):
    print(n1, "É MAIOR QUE", n2)

elif (n2 > n1):
    print(n2, "É MAIOR QUE", n1)

else:
    print(n1, "e", n2, "SÃO IGUAIS")       