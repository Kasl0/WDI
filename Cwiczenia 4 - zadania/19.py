from random import randint

def funkcja(tablica, iloczyn):
    par = 0
    for wiersz in range(len(tablica)):
        for kolumna in range(len(tablica)):
            if wiersz+2 < len(tablica) and kolumna-1 >= 0:
                par += (tablica[wiersz][kolumna] * tablica[wiersz+2][kolumna-1] == iloczyn)
            if wiersz+2 < len(tablica) and kolumna+1 < len(tablica):
                par += (tablica[wiersz][kolumna] * tablica[wiersz+2][kolumna+1] == iloczyn)
            if wiersz-1 >= 0 and kolumna+2 < len(tablica):
                par += (tablica[wiersz][kolumna] * tablica[wiersz-1][kolumna+2] == iloczyn)
            if wiersz+1 < len(tablica) and kolumna+2 < len(tablica):
                par += (tablica[wiersz][kolumna] * tablica[wiersz+1][kolumna+2] == iloczyn)
    return par
    
N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

for k in range(10):
    print(funkcja(T, k), end="")