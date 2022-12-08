from random import randint

def funkcja(tablica, k):
    for bok in range(3, len(tablica)+1, 2):
        for wiersz in range(len(tablica)-bok+1):
            for kolumna in range(len(tablica)-bok+1):
                if tablica[wiersz][kolumna] * tablica[wiersz+bok-1][kolumna] * tablica[wiersz][kolumna+bok-1] * tablica[wiersz+bok-1][kolumna+bok-1] == k:
                    return (True, wiersz+bok//2, kolumna+bok//2)
    return False
    
N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

for k in range(1,100):    
    if funkcja(T, k) != False:
        print(k, funkcja(T, k))