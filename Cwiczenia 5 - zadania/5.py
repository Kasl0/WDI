from random import randint

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

def potnij(t, od=0):
    n = len(t)
    i = od + 2
    while i <= n and i <= 30:
        liczba = 0
        for a in range(od, i):
            liczba = liczba * 2 + t[a]
        if czy_pierwsza(liczba):
            if (od !=0 and i == n) or potnij(t, i):
                return True
        i += 1
    return False

N = int(input("N="))
T = [randint(0,1) for _ in range(N)]

print(T)
print(potnij(T))