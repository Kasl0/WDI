from random import randint

def funkcja(tablica):
    maks = 0
    for kolumna in range(N):
        suma = 0
        for wiersz in range(N):
            suma += tablica[wiersz][kolumna]
        if suma > maks:
            maks = suma
            min_kolumny = kolumna

    min = float("inf")
    for wiersz in range(N):
        suma = 0
        for kolumna in range(N):
            suma += tablica[wiersz][kolumna]
        if suma < min:
            min = suma
            min_wiersza= wiersz
    
    return (min_wiersza, min_kolumny)

N = int(input("N="))
T = [[randint(1,100) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])
    
print(funkcja(T))