from random import randint
from math import sqrt

def podzial(T, A=(), B=(), p=0):
    if p == len(T):
        if A and B:
            x1 = 0
            y1 = 0
            for punkt in A:
                x1 += punkt[0]
                y1 += punkt[1]
            x1 /= len(A)
            y1 /= len(A)

            x2 = 0
            y2 = 0
            for punkt in B:
                x2 += punkt[0]
                y2 += punkt[1]
            x2 /= len(B)
            y2 /= len(B)
            return sqrt((x2-x1)**2 + (y2-y1)**2)
        return 10**9

    return min(podzial(T, A+(T[p],), B, p+1), podzial(T, A, B+(T[p],), p+1), podzial(T, A, B, p+1))
    

N = int(input("N="))
T = [(randint(1,1000)/100, randint(1,1000)/100) for _ in range(N)]
print(T)

print(podzial(T))