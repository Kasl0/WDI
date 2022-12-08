from random import randint
gs = 10**10

def ruch(T, w, k, s=0):
    global gs
    if w == 8:
        gs = min(gs, s)
    else:
        if k > 0:
            ruch(T, w+1, k-1, s+T[w][k])
        ruch(T, w+1, k, s+T[w][k])
        if k < 7:
            ruch(T, w+1, k+1, s+T[w][k])

T = [[randint(1,10) for _ in range(8)] for _ in range(8)]
for i in range(len(T)):
    print(T[i])

k = int(input("k="))
print(ruch(T, 0, k))
