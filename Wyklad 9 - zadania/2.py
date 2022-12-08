from random import randint

def qs(T, k, l, p):
    i = l
    j = p
    x = T[(1+p)//2]
    while i <= j:
        while T[i] < x:
            i += 1
        while T[j] > x:
            j -= 1
        if i <= j:
            T[j], T[i] = T[i], T[j]
            i += 1
            j -= 1
    if l < k <= j:
        qs(T, k, l, j)
    if i < k <= p:
        qs(T, k, i, p)

N = int(input("N="))
T = [randint(1,100) for _ in range(N)]
print(T)
k = int(input("k="))
qs(T, k, 0, N-1)
print(T)
suma = 0
for i in range(k):
    suma += T[k]
print(suma)