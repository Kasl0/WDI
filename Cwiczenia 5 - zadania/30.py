from random import randint
from math import sqrt

def czy_istnieje(T, r, k, podzbior=(), p=0):
    if p == len(T):
        n = len(podzbior)
        if 3 <= n < k:
            
            while n > 3:
                if n % 3 == 0:
                    n //= 3
                else:
                    return False

            n = len(podzbior)
            suma_x = 0
            suma_y = 0
            for punkt in podzbior:
                suma_x += punkt[0]
                suma_y += punkt[1]
            suma_x /= n
            suma_y /= n
            if sqrt(suma_x*suma_x + suma_y*suma_y) < r:
                return True
        return False
    
    return czy_istnieje(T, r, k, podzbior, p+1) or czy_istnieje(T, r, k, podzbior+(T[p],), p+1)

N = int(input("N="))
T = [(randint(-1000,1000)/100, randint(-1000,1000)/100) for _ in range(N)]
print(T)
r = int(input("r="))
k = int(input("k="))

print(czy_istnieje(T, r, k))