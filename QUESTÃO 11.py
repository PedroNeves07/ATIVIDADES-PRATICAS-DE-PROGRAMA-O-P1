n1 = int(input("DIGITE UM NUMERO:"))

if (( n1 % 2) == 0) and ( n1 > 0):
    print ("PAR E POSITIVO")

elif (( n1 % 2 ) == 0) and ( n1 < 0 ):
    print("PAR E NEGATIVO")

else:
    print("ÍMPAR")            