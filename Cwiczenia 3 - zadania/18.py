from random import randint

def funkcja(tab):
    maks = 0
    for i in range(N):
        for j in range(N-1, -1, -1):
            k = 0
            dlugosc = 0
            while i+k < N and j-k >= 0 and tab[i+k]%2 == 1 and tab[i+k] == tab[j-k]:
                k += 1
                dlugosc += 1
            if j-k+1 == i and dlugosc > maks:
                maks = dlugosc
    return maks

N = int(input("N="))
tablica = [randint(1, 999) for _ in range(N)]
print(tablica)
print(funkcja(tablica))