"""W pierwszym zadaniu była liczba naturalna
w ktorej można było "odcinać" liczby  z przodu i na końcu.
I trzeba było zwrócić największą liczbę pierwszą o różnych
cyfrach którą można w ten sposób uzyskać."""

def dlugosc(n):
    dl = 0
    while n > 0:
        dl += 1
        n //= 10
    return dl

def czy_pierwsza(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 2
    return True

def czy_rozne_cyfry(n):
    cyfry = [0 for _ in range(10)]
    while n > 0:
        cyfry[n%10] += 1
        n //= 10
    for i in range(10):
        if cyfry[i] > 1:
            return False
    return True

def szukaj(n):
    dl = dlugosc(n)
    maks = 0
    for przod in range(1, dl+1):
        for tyl in range(przod):
            liczba = (n % (10**przod)) // (10**tyl)
            if liczba > maks and czy_pierwsza(liczba) and czy_rozne_cyfry(liczba):
                maks = liczba
    return maks

n = int(input("n="))
print(szukaj(n))