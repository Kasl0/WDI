from random import randint

def funkcja(tablica):
    maks = 0
    for wiersz in range(len(tablica)):
        for kolumna in range(len(tablica)):
            suma = 0

            if wiersz-1 >= 0:
                suma += tablica[wiersz-1][kolumna]
                if kolumna-1 >= 0:
                    suma += tablica[wiersz-1][kolumna-1]
                if kolumna+1 < len(tablica):
                    suma += tablica[wiersz-1][kolumna+1]

            if wiersz+1 < len(tablica):
                suma += tablica[wiersz+1][kolumna]
                if kolumna-1 >= 0:
                    suma += tablica[wiersz+1][kolumna-1]
                if kolumna+1 < len(tablica):
                    suma += tablica[wiersz+1][kolumna+1]

            if kolumna-1 >= 0:
                suma += tablica[wiersz][kolumna-1]

            if kolumna+1 < len(tablica):
                suma += tablica[wiersz][kolumna+1]
            
            if suma > maks:
                maks = suma
                wiersz_maks = wiersz
                kolumna_maks = kolumna

    return (wiersz_maks, kolumna_maks)
    
N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

print(funkcja(T))