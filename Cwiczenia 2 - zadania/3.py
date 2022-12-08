def konwersja(liczba):
    liczba_binarna = ""
    while liczba > 0:
        if liczba % 2 == 1:
            liczba_binarna = "1" + liczba_binarna
            liczba //= 2
        else:
            liczba_binarna = "0" + liczba_binarna
            liczba //= 2
    return liczba_binarna

def czy_palindrom(n):
    return str(n) == str(n)[::-1]

def czy_palindrom_dwojkowy(n):
    return konwersja(n) == konwersja(n)[::-1]


n = int(input("n="))

print(czy_palindrom(n))
print(czy_palindrom_dwojkowy(n))