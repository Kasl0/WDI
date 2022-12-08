from random import randint

for N in range(20,41):
    ile = 0
    for i in range(10**4):
        rok = [0 for _ in range(365)]
        for _ in range(N):
            rok[randint(0, 364)] += 1
        for j in range(365):
            if rok[j] > 1:
                ile += 1
                break
    print(N, ": ", ile/(10**4), sep="")