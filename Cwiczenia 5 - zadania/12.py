from random import randint

def enek(T, iloczyn, akt=1, p=0, enki=()):
    if p == len(T):
        if iloczyn == akt:
            print(enki)
            return 1
        return 0
    if akt > iloczyn:
        return 0
    return enek(T, iloczyn, akt, p+1, enki) + enek(T, iloczyn, akt*T[p], p+1, enki+(T[p],))

N = int(input("N="))
T = [randint(0,10) for _ in range(N)]
print(T)

iloczyn = int(input("iloczyn="))
print(enek(T, iloczyn))