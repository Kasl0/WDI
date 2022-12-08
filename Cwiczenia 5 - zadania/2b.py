from random import randint

def waga(n):
    res = 0
    k = 2
    while n > 1 and k*k <= n:
        if n % k == 0:
            res += 1
            while n % k == 0:
                n //= k
        k += 1
    if n > 1:
        res += 1
    return res

def podziel(t, a=0, b=0, c=0, p=0):
    if p == len(t):
        return a==b==c
    return podziel(t, a+t[p], b, c, p+1) or podziel(t, a, b+t[p], c, p+1) or podziel(t, a, b, c+t[p], p+1)

def funkcja(t):
    suma = 0
    for i in range(len(T)):
        x = waga(T[i])
        suma += x
        T[i] = x
    if suma % 3 == 0:
        return podziel(T)
    else:
        return False

N = int(input("N="))
T = [randint(1,10) for _ in range(N)]

print(T)
print(funkcja(T))
