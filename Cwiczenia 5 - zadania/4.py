def skocz(t, x, y):
    t[x][y] = True
    n = len(t)

    if x+2 < n and y+1 < n and t[x+2][y+1] == False:
        skocz(t, x+2, y+1)
    if x+2 < n and y-1 >= 0 and t[x+2][y-1] == False:
        skocz(t, x+2, y-1)

    if x-2 >= 0 and y+1 < n and t[x-2][y+1] == False:
        skocz(t, x-2, y+1)
    if x-2 >= 0 and y-1 >= 0 and t[x-2][y-1] == False:
        skocz(t, x-2, y-1)

    if x+1 < n and y+2 < n and t[x+1][y+2] == False:
        skocz(t, x+1, y+2)
    if x+1 < n and y-2 >= 0 and t[x+1][y-2] == False:
        skocz(t, x+1, y-2)
    
    if x-1 >= 0 and y+2 < n and t[x-1][y+2] == False:
        skocz(t, x-1, y+2)
    if x-1 >= 0 and y-2 >= 0 and t[x-1][y-2] == False:
        skocz(t, x-1, y-2)


N = int(input("N="))
T = [[False for _ in range(N)] for _ in range(N)]

skocz(T, 0, 0)
print(*T, sep='\n')