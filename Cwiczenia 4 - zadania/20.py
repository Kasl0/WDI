from random import randint

def funkcja(tablica):
    maks = 0
    polozenie = 0
    for x in range(len(tablica)):
        for y in range(len(tablica)):
            for a in range(x+1, len(tablica)):
                for b in range(len(tablica)):
                    suma = 0
                    if y == b:
                        continue
                    for i in range(len(tablica)):
                        suma += tablica[x][i]
                        suma += tablica[i][y]
                        suma += tablica[a][i]
                        suma += tablica[i][b]
                    suma -= tablica[x][y]
                    suma -= tablica[a][b]
                    suma -= tablica[x][b]
                    suma -= tablica[a][y]
                if suma > maks:
                    maks = suma
                    polozenie = (x, y, a, b)
    return polozenie

N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

print(funkcja(T))