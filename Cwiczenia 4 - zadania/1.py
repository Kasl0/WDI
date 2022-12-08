def funkcja(T, N):
    naturalna = 1
    gora = 0
    dol = N-1
    prawa = N-1
    lewa = 0

    while naturalna <= N*N:
        for i in range(lewa, prawa+1):
            T[gora][i] = naturalna
            naturalna += 1
        gora += 1

        for i in range(gora, dol+1):
            T[i][prawa] = naturalna
            naturalna += 1
        prawa -= 1

        for i in range(prawa, lewa-1, -1):
            T[dol][i] = naturalna
            naturalna += 1
        dol -= 1

        for i in range(dol, gora-1, -1):
            T[i][lewa] = naturalna
            naturalna += 1
        lewa += 1

N = int(input("N="))
T = [[0 for _ in range(N)] for _ in range(N)]
funkcja(T, N)

for i in range(N):
    print(T[i])
