def oblicz(n):
    a = 1
    count = 0
    while a <= n:
        b = a
        while b <= n:
            c = b
            while c <= n:
                count += 1
                c *= 2
            b *= 3
        a *= 5
    return count

N = int(input("N="))
print(oblicz(N))