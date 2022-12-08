from random import randint

def funkcja(tablica):
    min_dodatnie = float("inf")
    min_ujemne = float("-inf")
    maks_dodatni = 0
    maks_ujemny = 0
    for a in range(N):
        suma_kolumny = 0
        suma_wiersza = 0
        for b in range(N):
            suma_kolumny += tablica[b][a]
            suma_wiersza += tablica[a][b]
        if suma_wiersza > 0 and suma_wiersza > maks_dodatni:
            maks_dodatni = suma_wiersza
            maks_dodatni_kolumna = a
        if suma_wiersza < 0 and suma_wiersza < maks_ujemny:
            maks_ujemny = suma_wiersza
            maks_ujemny_kolumna = a
        if suma_kolumny > 0 and suma_kolumny < min_dodatnie:
            min_dodatnie = suma_kolumny
            min_dodatnie_wiersz = b
        if suma_kolumny < 0 and suma_kolumny > min_ujemne:
            min_ujemne = suma_kolumny
            min_ujemne_wiersz = b

    if maks_dodatni / min_dodatnie > maks_ujemny / min_ujemne:
        return (maks_dodatni_kolumna, min_dodatnie_wiersz)
    else:
        return (maks_ujemny_kolumna, min_ujemne_wiersz)

N = int(input("N="))
T = [[randint(-10,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])
    
print(funkcja(T))