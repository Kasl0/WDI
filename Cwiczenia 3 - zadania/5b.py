wartosci = [0 for _ in range(10)]

n = int(input("n="))
while n != 0:
    for i in range(0, 10):
        if n > wartosci[i]:
            for j in range(9, i, -1):
                wartosci[j] = wartosci[j-1]
            wartosci[i] = n
            print(wartosci)
            break
    n = int(input("n="))
print(wartosci[9])