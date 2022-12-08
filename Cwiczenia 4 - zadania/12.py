from random import randint

def funkcja(tablica):
    elementow = [0 for _ in range(N)]
    for poziom in range(len(tablica)):
        for wiersz in range(1,len(tablica)-1):
            for kolumna in range(1,len(tablica)-1):
                zlozonych = 0
                zlozonych += czy_zlozona(tablica[poziom][wiersz-1][kolumna])
                zlozonych += czy_zlozona(tablica[poziom][wiersz-1][kolumna+1])
                zlozonych += czy_zlozona(tablica[poziom][wiersz-1][kolumna-1])
                zlozonych += czy_zlozona(tablica[poziom][wiersz+1][kolumna])
                zlozonych += czy_zlozona(tablica[poziom][wiersz+1][kolumna+1])
                zlozonych += czy_zlozona(tablica[poziom][wiersz+1][kolumna-1])
                if zlozonych < 6:
                    zlozonych += czy_zlozona(tablica[poziom][wiersz][kolumna+1])
                if zlozonych < 6:
                    zlozonych += czy_zlozona(tablica[poziom][wiersz][kolumna-1])
                if zlozonych >= 6:
                    elementow[poziom] += 1
        if poziom > 0 and elementow[poziom] != elementow[poziom-1]:
            return False
    return True

def czy_zlozona(n):
    if n < 4:
        return 0
    if n % 2 == 0:
        return 1
    i = 3
    while i**2 <= n:
        if n%i == 0:
            return 1
        i += 2
    return 0
    
N = int(input("N="))
T = [[[randint(1,10) for _ in range(N)] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(T[i][j])
    print()

print(funkcja(T))