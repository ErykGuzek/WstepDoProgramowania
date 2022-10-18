#(2.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała

litera = input ("Podaj litere: ")
if (len(litera)>1):
    print("Wprowadzono więcej niż 1 literę")
    exit()
if (len(litera)==0):
    print("Nie wprowadzono litery")
    exit()
if ("a"<=litera<="z"):
    print("Mała litera")
elif("A"<=litera<="Z") :
    print("Duża litera")
else:
    print("Nie jest literą")
