N = int(input("N="))
pierwsze = [True for _ in range(N)]
pierwsze[0] = False
pierwsze[1] = False

i = 2
while i*i <= N:
    if pierwsze[i]:
        k = 2
        while k * i < N:
            pierwsze[k*i] = False
            k += 1
    i += 1

for i in range(N):
    if pierwsze[i]:
        print(i, end=" ")
