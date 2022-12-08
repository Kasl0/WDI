ile = 0

def hetman(kol=[0 for _ in range(8)], skos1=[0 for _ in range(15)], skos2=[0 for _ in range(15)], wiersz=0):
    global ile

    for kolumna in range(8):
        if kol[kolumna] == skos1[kolumna-wiersz+7] == skos2[kolumna+wiersz] == 0:
            kol[kolumna] = skos1[kolumna-wiersz+7] = skos2[kolumna+wiersz] = 1
            if wiersz == 7:
                ile += 1
                break
            hetman(kol.copy(), skos1.copy(), skos2.copy(), wiersz+1)
            kol[kolumna] = skos1[kolumna-wiersz+7] = skos2[kolumna+wiersz] = 0

hetman()
print(ile)
