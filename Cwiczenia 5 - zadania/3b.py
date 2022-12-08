from random import randint

def ruch(T, w, k):
    if k < 0 or k >= 8:
        return 2**30
    if w == 8:
        return 0
    return min(ruch(T,w+1,k-1), ruch(T,w+1,k), ruch(T,w+1,k+1)) + T[w][k]

T = [[randint(1,10) for _ in range(8)] for _ in range(8)]
for i in range(len(T)):
    print(T[i])

k = int(input("k="))
print(ruch(T, 0, k))

