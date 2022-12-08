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

def funkcja(tablica):
    komplementarne  = [[False for _ in range(N)] for _ in range(N)]
    for wiersz in range(len(tablica)):
        for kolumna in range(len(tablica)):
            for a in range(wiersz, len(tablica)):
                for b in range(len(tablica)):
                    if a == wiersz and b == 0:
                        b = kolumna + 1
                        if b == len(tablica):
                            break
                    if czy_pierwsza(tablica[wiersz][kolumna] + tablica[a][b]):
                        komplementarne[wiersz][kolumna] = True
                        komplementarne[a][b] = True
            if komplementarne[wiersz][kolumna] == False:
                tablica[wiersz][kolumna] = 0

    
N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

funkcja(T)
print()

for i in range(N):
    print(T[i])