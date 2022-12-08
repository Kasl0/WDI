def skocz(T, w=0, k=0, n=1):
    N = len(T)
    if w < 0 or w >= N or k < 0 or k >= N:
        return
    if T[w][k] != 0:
        return
    T[w][k] = n
    for nw, nk in [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]:
        skocz(T, w+nw, k+nk, n+1)

N = int(input("N="))
T = [[0 for _ in range(N)] for _ in range(N)]

skocz(T)
print(*T, sep='\n')