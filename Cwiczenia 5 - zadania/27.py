from random import randint

def znajdz(T, kwadraty=(), i=0, ile=0, suma=0):
    if ile == 13 and suma == 2012:
        return True
    if i == len(T) or ile == 13 or suma >= 2012:
        return False

    if znajdz(T, kwadraty, i+1, ile, suma):
        return True

    for kwadrat in kwadraty:
        if not (kwadrat[1] <= T[i][0] or T[i][1] <= kwadrat[0] or kwadrat[3] <= T[i][2] or T[i][3] <= kwadrat[2]):
            return False

    return znajdz(T, kwadraty+(T[i],), i+1, ile+1, suma+(T[i][1]-T[i][0])*(T[i][3]-T[i][2]))

N = int(input("N="))
T = [(randint(1,5), randint(6,10), randint(1,5), randint(6,10)) for _ in range(N)]
print(T)

print(znajdz(T))