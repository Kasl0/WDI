"""Liczby są 4-zgodne jeżeli w systemie czwórkowym składają się z takich samych cyfr jak
w systemie dziesiętnym. Znajdź w tablicy t o długości n najdłuższy podciąg (niekoniecznie spójny),
który składa się z liczb 4-zgodnych."""

from random import randint

def funkcja(t):
    maks = 0
    cyfry = [[0 for _ in range(4)] for _ in range(len(t))]

    for i in range(len(t)):
        while t[i] > 0:
            cyfry[i][t[i] % 4] = True
            t[i] //= 4

    for i in range(len(t)):
        dlugosc = 0
        for j in range(len(t)):
            if cyfry[i] == cyfry[j]:
                dlugosc += 1
        if dlugosc > maks:
            maks = dlugosc
    return maks

n = int(input("n="))
t = [0 for _ in range(n)]
for i in range(n):
    t[i] = int(input("n="))

print(funkcja(t))