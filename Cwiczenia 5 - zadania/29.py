from random import randint
from math import sqrt

def czy_istnieje(T, r, podzbior=(), p=0):
    if p == len(T):
        if len(podzbior) >= 3:
            suma = [0, 0, 0]
            for punkt in podzbior:
                for i in range(3):
                    suma[i] += punkt[i]
            for i in range(3):
                suma[i] /= len(podzbior)
            if sqrt(suma[0]*suma[0] + suma[1]*suma[1] + suma[2]*suma[2]) <= r:
                return True
        return False
    
    return czy_istnieje(T, r, podzbior, p+1) or czy_istnieje(T, r, podzbior+(T[p],), p+1)

N = int(input("N="))
T = [(randint(-1000,1000)/100, randint(-1000,1000)/100, randint(-1000,1000)/100) for _ in range(N)]
print(T)
r = int(input("r="))

print(czy_istnieje(T, r))