from math import sqrt

def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma

dlugosc = 1

for n in range(1,1000000):
    suma = 0
    n_temp = n
    b = 2
    pierwsza = True
    while n_temp > 1 and b <= sqrt(n_temp):
        if n_temp % b == 0:
            pierwsza = False
            suma += suma_cyfr(b)
            n_temp //= b
        else:
            b += 1
    if n_temp > 1:
        suma += suma_cyfr(n_temp)

    if pierwsza == False and suma == suma_cyfr(n):
        print(n)