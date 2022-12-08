def hanoi(n, wieze):
    A, B, C = wieze
    if n > 0:
        hanoi(n-1, (A, C, B))
        ruch(A,C)
        hanoi(n-1, (B, A, C))
    return (A, B, C)

def ruch(X, Y):
    p = 0
    while X[p] == 0:
        p += 1
    q = 0
    while q < len(Y) and Y[q] == 0:
        q += 1
    q -= 1
    Y[q] = X[p]
    X[p] = 0

n = int(input("n="))
T = [i for i in range(1,n+1)]
wieze = (T, [0 for _ in range(n)], [0 for _ in range(n)])
print(*wieze, sep='\n')
print()
print(*hanoi(n, wieze), sep='\n')