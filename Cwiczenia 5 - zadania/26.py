def czy_zlozona(n):
    if n < 4:
        return False
    if n % 2 == 0:
        return True
    i = 3
    while i**2 <= n:
        if n%i == 0:
            return True
        i += 2
    return False

def zbuduj(A, B, liczba=0):
    if liczba == 0:
        A -= 1
        liczba = 1
    if A == B == 0:
        return czy_zlozona(liczba)

    if A > 0 and B > 0:
        return zbuduj(A-1, B, liczba*2+1) + zbuduj(A, B-1, liczba*2)
    elif A > 0:
        return zbuduj(A-1, B, liczba*2+1)
    elif B > 0:
        return zbuduj(A, B-1, liczba*2)


A = int(input("A="))
B = int(input("B="))

print(zbuduj(A, B))

