a = int(input("Podaj Liczbę"))
b = int(input("Podaj liczbę"))

if b<a:
    a,b=b,a

while b>=a:
    if a%2==0:
            print(a,end=' ')
            a=a+1
    else:
        a=a+1
        continue