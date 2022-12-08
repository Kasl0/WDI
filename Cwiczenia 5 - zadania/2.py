from random import randint

def waga(n):
    ile = 0
    dzielnik = 2
    ostatnio = 0
    while n > 1:
        if n % dzielnik == 0:
            n //= dzielnik
            if dzielnik != ostatnio:
                ile += 1
            ostatnio = dzielnik
        else:
            dzielnik += 1
    return ile

def podzial(a, b, c, tablica):
    if len(tablica)==0:
        return a==b and b==c
    if podzial(a+waga(tablica[0]), b, c, tablica[1:]):
        return True
    if podzial(a, b+waga(tablica[0]), c, tablica[1:]):
        return True
    if podzial(a, b, c+waga(tablica[0]), tablica[1:]):
        return True
    return False

N = int(input("N="))
T = [randint(1,10) for _ in range(N)]

print(T)
print(podzial(0, 0, 0, T))