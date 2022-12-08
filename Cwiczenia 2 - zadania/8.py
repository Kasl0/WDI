n = int(input("n="))

for c in range(n+1,2000):
    a = 1
    b = 1
    suma = 1

    while suma < c:
        suma += a
        a, b = a + b, a

    if suma != c:
        a = 1
        b = 1
        suma -= 1
        while suma > c:
            suma -= a
            a, b = a + b, a
        if suma != c:
            print(c)
            exit()