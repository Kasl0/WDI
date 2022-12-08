from random import randint

def funkcja(tab):
    maks = 0
    for i in range(N):
        czynniki_pierwsze = [0 for _ in range(1000)]
        dlugosc = 0
        flaga = False
        for j in range(i, N):
            b = 2
            n = tab[j]
            while n > 1 and b*b <= n:
                if n % b == 0:
                    if czynniki_pierwsze[b]:
                        flaga = True
                        break
                    czynniki_pierwsze[b] += 1
                    n //= b
                else:
                    b += 1
            if flaga:
                break
            if n > 1:
                if czynniki_pierwsze[n]:
                    break
                czynniki_pierwsze[n] += 1
            dlugosc += 1
        if maks < dlugosc:
            maks = dlugosc
    return maks

N = int(input("N="))
tablica = [randint(1, 999) for _ in range(N)]
print(tablica)
print(funkcja(tablica))