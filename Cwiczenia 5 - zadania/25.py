from random import randint

def przejscie(T, i=0, skokow=0):
    if i == len(T)-1:
        return skokow
    if i > len(T)-1:
        return -1

    b = 2
    n = T[i]
    while n > 1 and b*b <= n:
        if n % b == 0:
            res = przejscie(T, i+b, skokow+1)
            if res > 0:
                return res
            n //= b
        else:
            b += 1
    if n > 1 and n != T[i]:
        return przejscie(T, i+n, skokow+1)

N = int(input("N="))
T = [randint(1,100) for _ in range(N)]
print(T)

print(przejscie(T))