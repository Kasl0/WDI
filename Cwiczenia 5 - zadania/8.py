from random import randint

def odwaz(T, masa, p=0):
    if masa == 0:
        return True
    if p == len(T):
        return False
    return odwaz(T, masa, p+1) or odwaz(T, masa-T[p], p+1) or odwaz(T, masa+T[p], p+1)

N = int(input("N="))
T = [randint(0,10) for _ in range(N)]
print(T)

masa = int(input("odwaz="))
print(odwaz(T, masa))
