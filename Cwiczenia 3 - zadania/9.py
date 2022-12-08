from random import randint

def najdluzszy_podciag(tab):
    dlugosc = 1
    maks = 0
    for i in range(1, N):
        if tablica[i-1] < tablica[i]:
            dlugosc += 1
        else:
            if maks < dlugosc:
                maks = dlugosc
            dlugosc = 1
    return maks

N = int(input("N="))
tablica = [randint(1, 1000) for _ in range(N)]
print(tablica)
print(najdluzszy_podciag(tablica))


