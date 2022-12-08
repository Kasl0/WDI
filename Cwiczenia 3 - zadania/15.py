from random import randint

def czy_pierwsza(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 2
    return True

def funkcja(tab):
    pozostala_pierwsza = False
    a = 1
    b = 1

    if czy_pierwsza(tab[0]):
        pozostala_pierwsza = True

    while a < len(tab):
        if czy_pierwsza(tab[a]):
            return False
        if pozostala_pierwsza == False:
            for i in range(b+1, a):
                if czy_pierwsza(tab[i]):
                    pozostala_pierwsza = True
                    break
        a, b = a + b, a

    if pozostala_pierwsza == False:
        for i in range(b+1, len(tab)):
            if czy_pierwsza(tab[i]):
                pozostala_pierwsza = True
                break
    return pozostala_pierwsza

tablica = [randint(100, 999) for _ in range(100)]
print(funkcja(tablica))