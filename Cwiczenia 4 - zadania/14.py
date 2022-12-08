from random import randint

def funkcja(t1, t2):
    for x in range(len(t2) - len(t1) + 1):
        for y in range(len(t2) - len(t1) + 1):
            ile = 0
            for a in range(len(t1)):
                for b in range(len(t1)):
                    ile += czy_zgodne(t1[a][b], t2[x+a][y+b])
            if ile > len(t1)*len(t1)/3:
                return True
    return False

def czy_zgodne(a, b):
    suma = 0
    while a > 0:
        suma += a % 2
        a //= 2
    while b > 0:
        suma -= b % 2
        b //= 2
    if suma == 0:
        return 1
    else:
        return 0
    
N1 = int(input("N1="))
T1 = [[randint(1,10) for _ in range(N1)] for _ in range(N1)]
for i in range(N1):
    print(T1[i])

N2 = int(input("N2="))
T2 = [[randint(1,10) for _ in range(N2)] for _ in range(N2)]
for i in range(N2):
    print(T2[i])

print(funkcja(T1,T2))