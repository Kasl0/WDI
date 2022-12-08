from random import randint

def funkcja(tablica):
    maks = 0
    for a in range(N):
        suma_kolumny = 0
        suma_wiersza = 0
        for b in range(N):
            suma_kolumny += tablica[b][a]
            suma_wiersza += tablica[a][b]
            if b > 9:
                suma_kolumny -= tablica[b-10][a]
                suma_wiersza -= tablica[a][b-10]
        if suma_kolumny > maks:
            maks = suma_kolumny
        if suma_wiersza > maks:
            maks = suma_wiersza
    return maks
    
N = int(input("N="))
T = [[randint(-10,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

print(funkcja(T))