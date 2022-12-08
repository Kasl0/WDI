from random import randint

def wyznacznik(T):
    n = len(T)
    if n == 1:
        return T[0][0]
    suma = 0
    for i in range(n):
        suma += T[0][i] * (-1)**(1+i+1) * wyznacznik(minor(T, 0, i))
    return suma

def minor(T, i, j):
    n = len(T)
    M = [[0 for _ in range(n-1)] for _ in range(n-1)]
    for a in range(n):
        if a < i:
            for b in range(n):
                if b < j:
                    M[a][b] = T[a][b]
                elif b > j:
                    M[a][b-1] = T[a][b]
        elif a > i:
            for b in range(n):
                if b < j:
                    M[a-1][b] = T[a][b]
                elif b > j:
                    M[a-1][b-1] = T[a][b]
    return M

N = int(input("N="))
T = [[randint(1,10) for _ in range(N)] for _ in range(N)]
print(*T, sep='\n')

print(wyznacznik(T))