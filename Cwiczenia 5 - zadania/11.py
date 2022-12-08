from random import randint

def enek(T, iloczyn, akt=1, p=0):
    if p == len(T):
        return iloczyn == akt
    if akt > iloczyn:
        return 0
    return enek(T, iloczyn, akt, p+1) + enek(T, iloczyn, akt*T[p], p+1)

N = int(input("N="))
T = [randint(0,10) for _ in range(N)]
print(T)

iloczyn = int(input("iloczyn="))
print(enek(T, iloczyn))