from random import randint

def funkcja(tablica):
    maks_dodatni = 0
    maks_ujemny = 0
    for kolumna in range(N):
        suma = 0
        for wiersz in range(N):
            suma += tablica[wiersz][kolumna]
        if suma > 0 and suma > maks_dodatni:
            maks_dodatni = suma
            maks_dodatni_kolumna = kolumna
        if suma < 0 and suma < maks_ujemny:
            maks_ujemny = suma
            maks_ujemny_kolumna = kolumna

    min_dodatnie = float("inf")
    min_ujemne = float("-inf")
    for wiersz in range(N):
        suma = 0
        for kolumna in range(N):
            suma += tablica[wiersz][kolumna]
        if suma > 0 and suma < min_dodatnie:
            min_dodatnie = suma
            min_dodatnie_wiersz = wiersz
        if suma < 0 and suma > min_ujemne:
            min_ujemne = suma
            min_ujemne_wiersz = wiersz
    
    if maks_dodatni / min_dodatnie > maks_ujemny / min_ujemne:
        return (maks_dodatni_kolumna, min_dodatnie_wiersz)
    else:
        return (maks_ujemny_kolumna, min_ujemne_wiersz)

N = int(input("N="))
T = [[randint(-10,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])
    
print(funkcja(T))