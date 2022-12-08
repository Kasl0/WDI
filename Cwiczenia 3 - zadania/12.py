from random import randint

def najdluzszy_podciag(tab, rosnacy):
    dlugosc = 1
    maks = 0
    ostatnia = -1
    for i in range(1, N):
        if tab[i-1] - tab[i] == ostatnia:
            if rosnacy and tab[i-1] - tab[i] < 0:
                dlugosc += 1
            elif not rosnacy and tab[i-1] - tab[i] > 0:
                dlugosc += 1
        else:
            if maks < dlugosc:
                maks = dlugosc
            dlugosc = 1
        ostatnia = tab[i-1] - tab[i]
    return maks + 1

N = int(input("N="))
tablica = [randint(1, 50) * 2 - 1 for _ in range(N)]
print(tablica)
print(abs(najdluzszy_podciag(tablica, True) - najdluzszy_podciag(tablica, False)))