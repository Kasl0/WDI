from random import randint

def funkcja(tablica):
    for a in range(len(tablica)):
        wiersz = False
        kolumna = False
        for b in range(len(tablica)):
            if tablica[a][b] == 0:
                wiersz = True
            if tablica[b][a] == 0:
                kolumna = True
            if wiersz and kolumna:
                break
        else:
            return False
    return True
    
N = int(input("N="))
T = [[randint(-1,1) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

print(funkcja(T))