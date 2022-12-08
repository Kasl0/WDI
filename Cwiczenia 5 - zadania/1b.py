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

def dopisz(liczba, reszta):
    if reszta == 0:
        if liczba // 10 and czy_pierwsza(liczba):
            print(liczba)
    else:
        dopisz(liczba, reszta // 10)
        dopisz(reszta%10*10**(dlugosc(liczba)) + liczba, reszta // 10)

dopisz(0, 1234)