def suma(n):
    tab = [0 for _ in range(20)]
    ile = 0
    k = 2
    while n > 1:
        if n % k == 0:
            tab[ile] = k
            ile += 1
            while n % k == 0:
                n //= k
        k += 1
    return rek(tab, ile)

def rek(T, ile, iloczyn=1, p=0):
    if p == ile:
        if iloczyn == 1:
            return 0
        return iloczyn

    return rek(T, ile, iloczyn, p+1) + rek(T, ile, iloczyn*T[p], p+1)

n = int(input("n="))
print(suma(n))