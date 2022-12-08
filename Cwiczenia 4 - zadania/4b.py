from random import randint

def funkcja(tablica):
    min = float("inf")
    maks = 0
    for a in range(N):
        suma_kolumny = 0
        suma_wiersza = 0
        for b in range(N):
            suma_kolumny += tablica[b][a]
            suma_wiersza += tablica[a][b]
        if suma_kolumny > maks:
            maks = suma_kolumny
            min_kolumny = a
        if suma_wiersza < min:
            min = suma_wiersza
            min_wiersza = b
    return (min_wiersza, min_kolumny)

N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])
    
print(funkcja(T))