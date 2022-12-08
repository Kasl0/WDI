from random import randint

def funkcja(tablica):
    maks = sprawdz(0, 0, tablica)
    for a in range(1, N):
        temp = sprawdz(a, 0, tablica)
        if temp > maks:
            maks = temp
        temp = sprawdz(0, a, tablica)
        if temp > maks:
            maks = temp
    if maks >= 3:
        return (True, maks)
    else:
        return (False, maks)

def sprawdz(x, y, tablica):
    dlugosc = 1
    x += 1
    y += 1
    if x < len(tablica) and y < len(tablica):
        q = tablica[x][y]/tablica[x-1][y-1]
        dlugosc += 1
        x += 1
        y += 1
    while x < len(tablica) and y < len(tablica):
        if tablica[x][y]/tablica[x-1][y-1] != q:
            break
        dlugosc += 1
        x += 1
        y += 1
    return dlugosc
    
N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]

for i in range(N):
    print(T[i])
    
print(funkcja(T))