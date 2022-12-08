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

def dlugosc(n):
    dl = 0
    while n > 0:
        n //= 10
        dl += 1
    return dl

pierwsze = {}
def wykresl(n):
    dl = dlugosc(n)
    if  dl < 3:
        return
    for a in range(1, dl+1):
        liczba = n // (10**a) * (10**(a-1)) + n % (10**(a-1))
        if czy_pierwsza(liczba):
            if not (liczba in pierwsze and pierwsze[liczba]):
                print(liczba)
                pierwsze[liczba] = True
        wykresl(liczba)

wykresl(12345)