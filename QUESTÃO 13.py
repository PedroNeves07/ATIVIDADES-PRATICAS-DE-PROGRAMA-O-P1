#. Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro

a = int(input("DIGA UM NUMERO:"))
m = a / 2 
d = a * 2 

if ( a > 100 ):
    print(m)

elif ( a < 100):
    print(d)
