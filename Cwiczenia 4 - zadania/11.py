from random import randint

def funkcja(tablica):
    ile = 0
    for wiersz in range(len(tablica)):
        for kolumna in range(len(tablica)):
            cyfry = False

            if wiersz-1 >= 0:
                if cyfry == False:
                    cyfry = zbior(tablica[wiersz-1][kolumna])
                elif cyfry != zbior(tablica[wiersz-1][kolumna]):
                    continue

            if kolumna-1 >= 0:
                if cyfry == False:
                    cyfry = zbior(tablica[wiersz][kolumna-1])
                elif cyfry != zbior(tablica[wiersz][kolumna-1]):
                    continue

            if wiersz+1 < len(tablica):
                if cyfry == False:
                    cyfry = zbior(tablica[wiersz+1][kolumna])
                elif cyfry != zbior(tablica[wiersz+1][kolumna]):
                    continue

            if kolumna+1 < len(tablica):
                if cyfry == False:
                    cyfry = zbior(tablica[wiersz][kolumna+1])
                elif cyfry != zbior(tablica[wiersz][kolumna+1]):
                    continue
            ile += 1
    return ile

def zbior(n):
    cyfry = [False for _ in range(10)]
    while n > 0:
        cyfry[n % 10] = True
        n //= 10
    return cyfry
    
N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])

print(funkcja(T))