from random import randint

def odwaz(T, masa, p=0, jakie=()):
    if masa == 0:
        print(jakie)
        return True
    if p == len(T):
        return False
    return odwaz(T, masa, p+1, jakie) or odwaz(T, masa-T[p], p+1, jakie+(T[p],)) or odwaz(T, masa+T[p], p+1, jakie+(T[p],))

N = int(input("N="))
T = [randint(0,10) for _ in range(N)]
print(T)

masa = int(input("odwaz="))
print(odwaz(T, masa))