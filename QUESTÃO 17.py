#Leia idade e: Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+).

n1 = int(input('INFORME UM NUMERO'))

if (( n1 % 2) == 0) and ( n1 > 0):
    print('PAR POSITIVO')

elif(( n1 % 2) == 0) and ( n1 < 0):
    print("PAR NEGATIVO")

elif((n1 % 2 ) > 0) and ( n1 > 0):
    print("ÍMPAR POSITIVO")

elif(( n1 % 2) > 0) and ( n1 < 0):
    print("ÍMPAR NEGATIVO")

else:
    print("NEUTRO")             


