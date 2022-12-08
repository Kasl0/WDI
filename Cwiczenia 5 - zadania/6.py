from random import randint

def szukaj(t, od=0, elementow=0, suma_elementow=0, suma_indeksow=0):
    if suma_elementow == suma_indeksow and suma_elementow != 0:
        return suma_elementow

    n = len(t)
    min_suma = 0
    min = float('inf')

    for i in range(od, n):
        if elementow + 1 < min:
            x = szukaj(t, i+1, elementow+1, suma_elementow+t[i], suma_indeksow+i)
            if x:
                min = elementow + 1
                min_suma = x
    return min_suma
    
#N = int(input("N="))
#T = [randint(0,100) for _ in range(N)]
T = [1,7,3,5,11,2]

print(T)
print(szukaj(T))