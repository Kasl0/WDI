c = int(input("c="))

a = 1
b = 1
suma = 1

while suma < c:
    suma += a
    a, b = a + b, a

if suma == c:
    print("istnieje")

else:
    a = 1
    b = 1
    suma -= 1
    while suma > c:
        suma -= a
        a, b = a + b, a
    if suma == c:
        print("istnieje")
    else:
        print("nie istnieje")