def rewers(n):
    return int(str(n)[::-1])

for n in range(1,200):
    nn = n
    while n != rewers(n):
        n += rewers(n)
    print(nn, n)

