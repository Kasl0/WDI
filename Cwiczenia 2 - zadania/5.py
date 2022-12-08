def konwersja(liczba, dlugosc):
    liczba_binarna = ""
    while liczba > 0:
        if liczba % 2 == 1:
            liczba_binarna = "1" + liczba_binarna
            liczba //= 2
        else:
            liczba_binarna = "0" + liczba_binarna
            liczba //= 2
    while len(liczba_binarna) < dlugosc:
        liczba_binarna = "0" + liczba_binarna
    return liczba_binarna

n = int(input("n="))
dlugosc = len(str(n))

suma = 0
for i in range(1, 2**dlugosc):
    substring = ""
    for j in range(0, dlugosc):
        if konwersja(i, dlugosc)[j] == "1":
            substring += str(n)[j]
    if (int(substring) % 7) == 0:
        suma += 1
        #print(substring)
        
print(suma)

