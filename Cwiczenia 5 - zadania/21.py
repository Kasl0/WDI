from random import randint

def podzbior(T, suma, wiersz=0, k_byly=()):
    if suma == 0:
        return True
    if suma < 0 or wiersz > 7:
        return False

    for kolumna in range(8):
        if kolumna not in k_byly and podzbior(T, suma-T[wiersz][kolumna], wiersz+1, k_byly+(kolumna,)):
            return True
    return podzbior(T, suma, wiersz+1)

T = [[randint(1,100) for _ in range(8)] for _ in range(8)]

for i in range(8):
    print(T[i])

suma = int(input("suma="))
print(podzbior(T,suma))

