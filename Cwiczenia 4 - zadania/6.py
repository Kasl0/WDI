from random import randint

def funkcja():
    dlugosc = 0
    for lista in T1:
        for liczba in lista:
            for i in range(0, N*N):
                if T2[i] == liczba:
                    break
                elif T2[i] == 0:
                    T2[i] = liczba
                    dlugosc += 1
                    break
                elif liczba < T2[i]:
                    for j in range(dlugosc, i, -1):
                        T2[j] = T2[j - 1]
                    T2[i] = liczba
                    dlugosc += 1
                    break

N = int(input("N="))
T1 = [[randint(1,100) for _ in range(N)] for _ in range(N)]
T2 = [0 for _ in range(N*N)]

for i in range(N):
    T1[i].sort()

for i in range(N):
    print(T1[i])

funkcja()
print(T2)