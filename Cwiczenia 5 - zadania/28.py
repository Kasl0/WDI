from random import randint

def czy_mozliwy(T):
    for i in range(len(T)):
        n = 0
        while T[i] > 0:
            n += T[i] % 2
            T[i] //= 2
        T[i] = n
    return podziel(T)

def podziel(T, a=0, b=0, c=0, p=0):
    if p == len(T):
        return a==b==c

    return podziel(T, a+T[p], b, c, p+1) or podziel(T, a, b+T[p], c, p+1) or podziel(T, a, b, c+T[p], p+1)

N = int(input("N="))
T = [randint(1,100) for _ in range(N)]
print(T)
print(czy_mozliwy(T))