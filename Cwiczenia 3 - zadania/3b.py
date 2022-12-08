from math import isqrt

def sito(n):
    pierwsze = [True for _ in range(n)]
    pierwsze[0] = pierwsze[1] = False

    for i in range(2, isqrt(n)+1): #isqrt(n) == int(sqrt(n))
        if pierwsze[i]:
            for j in range(i*i, n, i):
                pierwsze[j] = False
                
    for i in range(n):
        if pierwsze[i]:
            print(i, end=" ")

N = int(input("N="))
sito(N)