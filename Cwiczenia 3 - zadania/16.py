from random import randint

def czy_dokladnie_jeden(tab):
    mini = min(tab)
    maks = max(tab)
    ile_mini = 0
    ile_maks = 0
    for i in range(len(tab)):
        if tab[i] == maks:
            ile_maks += 1
        if tab[i] == mini:
            ile_mini += 1
    return ile_mini == 1 and ile_maks == 1

n = int(input("n="))
tablica = [randint(100, 999) for _ in range(n)]
print(czy_dokladnie_jeden(tablica))