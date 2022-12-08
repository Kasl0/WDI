from random import randint

def funkcja(tab):
    maks = 0
    for i in range(len(tab)):
        suma_elementow = 0
        suma_indeksow = 0
        for j in range(i, len(tab)):
            if j > i and tab[j-1] >= tab[j]:
                break
            suma_elementow += tab[j]
            suma_indeksow += j
            if suma_elementow == suma_indeksow and maks < j - i + 1:
                    maks = j - i + 1
    return maks

N = int(input("N="))
tablica = [randint(1, 10) for _ in range(N)]
print(tablica)
print(funkcja(tablica))